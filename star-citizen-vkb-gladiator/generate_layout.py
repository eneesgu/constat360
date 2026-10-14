#!/usr/bin/env python3
"""Génère le profil Star Citizen pour un VKB Gladiator NXT EVO (main droite).

Les options possibles pour chaque commande sont dans options.json ; les choix
faits sont dans choices.json ({"A3_PUSH": "scan_mode", ...}). Une commande
absente de choices.json prend l'option recommandée ; "none" la laisse vide.

Usage :
    python3 generate_layout.py
    python3 generate_layout.py --check defaultProfile.xml
        # vérifie en plus chaque action contre le defaultProfile.xml du jeu
        # (Data/Libs/Config/defaultProfile.xml extrait du Data.p4k)

Numérotation des boutons = profil d'usine VKB du Gladiator NXT EVO R (grip SCG).
"""
import argparse
import json
import os
import sys
import xml.etree.ElementTree as ET

HERE = os.path.dirname(os.path.abspath(__file__))
PROFILE_NAME = "VKB_NXT_EVO_R_FR"
JS = "js1"
PRODUCT = " VKBsim Gladiator EVO R    {0200231D-0000-0000-0000-504944564944}"

# Assignations joystick par défaut de Star Citizen 4.10.2 (axes de vol, boutons, chapeaux).
# Celles qui tombent sur une entrée utilisée par le profil sont effacées, sauf
# dans les menus, le mode spectateur, à pied et en véhicule terrestre.
GAME_DEFAULTS = [
    ("spaceship_movement", "v_pitch", "y"),
    ("spaceship_movement", "v_yaw", "x"),
    ("spaceship_movement", "v_roll", "rotz"),
    ("spaceship_movement", "v_strafe_up", "button9"),
    ("spaceship_movement", "v_strafe_down", "button10"),
    ("spaceship_movement", "v_strafe_left", "hat1_left"),
    ("spaceship_movement", "v_strafe_right", "hat1_right"),
    ("spaceship_movement", "v_afterburner", "button8"),
    ("spaceship_movement", "v_toggle_landing_system", "button12"),
    ("spaceship_movement", "v_autoland", "button12"),
    ("spaceship_quantum", "v_toggle_qdrive_engagement", "button1"),
    ("spaceship_scanning", "v_inc_scan_focus_level", "button3"),
    ("spaceship_scanning", "v_dec_scan_focus_level", "button4"),
    ("spaceship_mining", "v_toggle_mining_laser_fire", "button1"),
    ("spaceship_mining", "v_toggle_mining_laser_type", "button2"),
    ("spaceship_mining", "v_increase_mining_throttle", "button3"),
    ("spaceship_mining", "v_decrease_mining_throttle", "button4"),
    ("spaceship_salvage", "v_salvage_toggle_fire_focused", "button1"),
    ("spaceship_weapons", "v_weapon_preset_attack", "button1"),
    ("spaceship_weapons", "v_weapon_preset_next", "button1"),
    ("spaceship_weapons", "v_weapon_preset_prev", "button1"),
    ("spaceship_missiles", "v_weapon_toggle_launch_missile", "button1"),
    ("spaceship_missiles", "v_weapon_cycle_missile_fwd", "button2"),
    ("spaceship_defensive", "v_weapon_countermeasure_decoy_launch", "button3"),
    ("spaceship_defensive", "v_weapon_countermeasure_noise_launch", "button5"),
    ("player_choice", "pc_interaction_mode", "button6"),
    ("player_choice", "pc_focus", "button7"),
]

# Ordre des actionmaps = ordre du defaultProfile.xml du jeu (4.10)
MAP_ORDER = [
    "seat_general", "spaceship_general", "vehicle_mfd", "spaceship_view", "spaceship_movement",
    "spaceship_quantum", "spaceship_docking", "spaceship_targeting", "spaceship_targeting_advanced",
    "spaceship_target_hailing", "spaceship_radar", "spaceship_scanning", "spaceship_mining",
    "spaceship_salvage", "turret_movement", "turret_advanced", "spaceship_weapons", "spaceship_missiles",
    "spaceship_defensive", "spaceship_auto_weapons", "spaceship_power", "spaceship_hud",
    "lights_controller", "vehicle_mobiglas", "vehicle_general", "vehicle_driver", "player_choice",
]
MAP_CATEGORY = {
    "seat_general": "@ui_CCSeatGeneral", "spaceship_quantum": "@ui_CCSeatGeneral",
    "spaceship_docking": "@ui_CCSeatGeneral", "turret_movement": "@ui_CCTurrets",
    "turret_advanced": "@ui_CCTurrets", "lights_controller": "@ui_CGLightControllerDesc",
    "vehicle_general": "@ui_CCVehicle", "vehicle_driver": "@ui_CCVehicle",
    "player_choice": "@ui_CGInteraction",
}


def slot_inputs(js):
    """'button10' -> ['button10'] ; 'button23/24' -> ['button23', 'button24']."""
    if "/" in js:
        first, second = js.split("/")
        prefix = first.rstrip("0123456789")
        return [first, second if not second.isdigit() else prefix + second]
    return [js]


def load_bindings():
    with open(os.path.join(HERE, "options.json"), encoding="utf-8") as f:
        options = json.load(f)
    choices = {}
    path = os.path.join(HERE, "choices.json")
    if os.path.exists(path):
        with open(path, encoding="utf-8") as f:
            choices = json.load(f)
    bindings = []  # (map, action, input, slot)
    inverts = []   # groupes d'options du jeu à inverser (ex. flight_move_roll)
    for control in options["controls"]:
        pool = {o["id"]: o for o in control["pool"]}
        for slot in control["slots"]:
            chosen = choices.get(slot["slot"], slot["recommended_id"])
            if chosen == "none":
                continue
            if chosen not in pool:
                sys.exit(f"{slot['slot']} : option inconnue '{chosen}'")
            opt = pool[chosen]
            inverts += [g for g in opt.get("invert", []) if g not in inverts]
            inputs = slot_inputs(slot["js"])
            for a in opt["actions"]:
                bindings.append((a["map"], a["action"], inputs[0], slot["slot"]))
            if len(inputs) > 1:
                for a in opt.get("actions_b", []):
                    bindings.append((a["map"], a["action"], inputs[1], slot["slot"]))
    return bindings, inverts


def validate(bindings):
    seen = {}
    ok = True
    for m, a, inp, slot in bindings:
        prev = seen.get((m, a))
        if prev and prev[0] != inp:
            print(f"DOUBLON : {m}/{a} sur {prev[1]} et {slot} (le jeu n'accepte qu'un bouton par action)")
            ok = False
        seen[(m, a)] = (inp, slot)
    return ok


def with_clears(bindings):
    used_inputs = {inp for _, _, inp, _ in bindings}
    rebound = {(m, a) for m, a, _, _ in bindings}
    clears = [(m, a, None, "clear") for m, a, inp in GAME_DEFAULTS
              if inp in used_inputs and (m, a) not in rebound]
    return bindings + clears


def build_xml(bindings, inverts=()):
    by_map = {}
    for m, a, inp, _ in bindings:
        rebind = f"{JS}_ " if inp is None else f"{JS}_{inp}"
        by_map.setdefault(m, {}).setdefault(a, [])
        if rebind not in by_map[m][a]:
            by_map[m][a].append(rebind)
    unknown = set(by_map) - set(MAP_ORDER)
    if unknown:
        sys.exit(f"actionmap(s) absente(s) de MAP_ORDER : {sorted(unknown)}")
    cats = []
    for m in MAP_ORDER:
        if m in by_map:
            c = MAP_CATEGORY.get(m, "@ui_CCSpaceFlight")
            if c not in cats:
                cats.append(c)
    out = [f'<ActionMaps version="1" optionsVersion="2" rebindVersion="2" profileName="{PROFILE_NAME}">',
           f' <CustomisationUIHeader label="{PROFILE_NAME}" description="" image="">',
           '  <devices>', '   <keyboard instance="1"/>', '   <mouse instance="1"/>',
           '   <joystick instance="1"/>', '  </devices>', '  <categories>']
    out += [f'   <category label="{c}"/>' for c in cats]
    out += ['  </categories>', ' </CustomisationUIHeader>',
            ' <options type="keyboard" instance="1" Product="Keyboard  {6F1D2B61-D5A0-11CF-BFC7-444553540000}"/>',
            ]
    if inverts:
        out.append(f' <options type="joystick" instance="1" Product="{PRODUCT}">')
        out += [f'  <{g} invert="1"/>' for g in inverts]
        out.append(' </options>')
    else:
        out.append(f' <options type="joystick" instance="1" Product="{PRODUCT}"/>')
    out.append(' <modifiers />')
    for m in MAP_ORDER:
        if m not in by_map:
            continue
        out.append(f' <actionmap name="{m}">')
        for action in sorted(by_map[m]):
            out.append(f'  <action name="{action}">')
            out += [f'   <rebind input="{r}"/>' for r in by_map[m][action]]
            out.append('  </action>')
        out.append(' </actionmap>')
    out.append('</ActionMaps>')
    return "\n".join(out) + "\n"


def check_names(bindings, default_profile):
    root = ET.parse(default_profile).getroot()
    known = {(am.get("name"), a.get("name")) for am in root.iter("actionmap") for a in am.findall("action")}
    bad = [(m, a) for m, a, _, _ in bindings if (m, a) not in known]
    for m, a in bad:
        print(f"INCONNU dans le jeu : {m}/{a}")
    return not bad


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", metavar="defaultProfile.xml")
    ap.add_argument("--out", default=os.path.join(HERE, f"layout_{PROFILE_NAME}_exported.xml"))
    args = ap.parse_args()
    bindings, inverts = load_bindings()
    ok = validate(bindings)
    full = with_clears(bindings)
    if args.check:
        ok = check_names(full, args.check) and ok
    if not ok:
        sys.exit(1)
    xml = build_xml(full, inverts)
    ET.fromstring(xml)
    with open(args.out, "w", encoding="utf-8", newline="\r\n") as f:
        f.write(xml)
    print("Assignations :")
    for m, a, inp, slot in full:
        print(f"  {slot:10s} js1_{inp or '(effacé)':14s} {m}/{a}")
    print(f"\nÉcrit : {args.out}")


if __name__ == "__main__":
    main()
