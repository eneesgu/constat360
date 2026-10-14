#!/usr/bin/env python3
"""Génère le profil Star Citizen pour un VKB Gladiator NXT EVO (main droite).

Usage :
    python3 generate_layout.py                      # écrit le fichier XML à côté de ce script
    python3 generate_layout.py --check defaultProfile.xml
        # vérifie en plus chaque nom d'action contre le defaultProfile.xml du jeu
        # (Data/Libs/Config/defaultProfile.xml extrait du Data.p4k) et liste les
        # conflits avec les assignations joystick par défaut.

Numérotation des boutons = profil d'usine VKB du Gladiator NXT EVO R (grip SCG).
Si tu as modifié ton joystick dans VKBDevCfg, adapte la table BUTTONS ci-dessous.
"""
import argparse
import os
import sys
import xml.etree.ElementTree as ET

PROFILE_NAME = "VKB_NXT_EVO_R_FR"
JS = "js1"
PRODUCT = " VKBsim Gladiator EVO R    {0200231D-0000-0000-0000-504944564944}"

# Étiquette physique -> entrée DirectInput (profil d'usine VKB)
BUTTONS = {
    "TRIG1": "button1",   # gâchette, 1er cran
    "TRIG2": "button2",   # gâchette, 2e cran
    "A2": "button3",      # gros bouton rouge
    "B1": "button4",      # bouton index, avant de la tête
    "D1": "button5",      # bouton auriculaire (petit doigt)
    "A3_UP": "button6", "A3_RIGHT": "button7", "A3_DOWN": "button8", "A3_LEFT": "button9", "A3_PUSH": "button10",
    "A4_UP": "button11", "A4_RIGHT": "button12", "A4_DOWN": "button13", "A4_LEFT": "button14", "A4_PUSH": "button15",
    "C1_UP": "button16", "C1_RIGHT": "button17", "C1_DOWN": "button18", "C1_LEFT": "button19", "C1_PUSH": "button20",
    "RF_UP": "button21", "RF_DOWN": "button22",       # levier "rapid fire" sous B1
    "EN1_A": "button23", "EN1_B": "button24",         # encodeur EN1 (un sens / l'autre)
    "SW1_UP": "button25", "SW1_DOWN": "button26",     # interrupteur à rappel SW1
    "F1": "button27", "F2": "button28", "F3": "button29",
    "A1_UP": "hat1_up", "A1_RIGHT": "hat1_right", "A1_DOWN": "hat1_down", "A1_LEFT": "hat1_left",  # mini-stick A1 en mode chapeau
    "X": "x", "Y": "y", "TWIST": "rotz", "WHEEL": "z",  # axes ; WHEEL = molette des gaz sur le socle
}

# (actionmap, action, contrôle) — une ligne par assignation. None = efface l'assignation joystick par défaut.
BINDINGS = [
    # --- Axes
    ("spaceship_movement", "v_pitch", "Y"),
    ("spaceship_movement", "v_yaw", "X"),
    ("spaceship_movement", "v_roll", "TWIST"),
    ("spaceship_movement", "v_ifcs_speed_limiter_abs", "WHEEL"),

    # --- Gâchette (1er cran) : tire / lance / saute selon le mode actif
    ("spaceship_weapons", "v_weapon_preset_attack", "TRIG1"),
    ("spaceship_missiles", "v_weapon_toggle_launch_missile", "TRIG1"),
    ("spaceship_quantum", "v_toggle_qdrive_engagement", "TRIG1"),
    ("spaceship_scanning", "v_scanning_trigger_scan", "TRIG1"),
    ("spaceship_mining", "v_toggle_mining_laser_fire", "TRIG1"),
    ("spaceship_salvage", "v_salvage_toggle_fire_focused", "TRIG1"),
    # 2e cran : volontairement libre (par défaut le jeu y mettait "missile suivant", ce qui
    # changeait de missile à chaque tir appuyé à fond)

    # --- A2 (rouge) : mode missiles on/off
    ("seat_general", "v_toggle_missile_mode", "A2"),

    # --- B1 : verrou cardan (canons) / type de missile (missiles) / type de laser (minage)
    ("spaceship_weapons", "v_weapon_gimbals_state_toggle", "B1"),
    ("spaceship_missiles", "v_weapon_cycle_missile_fwd", "B1"),
    ("spaceship_mining", "v_toggle_mining_laser_type", "B1"),

    # --- D1 (petit doigt) : boost
    ("spaceship_movement", "v_afterburner", "D1"),
    ("vehicle_driver", "v_boost", "D1"),

    # --- A3 (chapeau central) : ciblage
    ("spaceship_targeting_advanced", "v_target_cycle_in_view_fwd", "A3_PUSH"),    # = touche T
    ("spaceship_targeting_advanced", "v_target_cycle_in_view_reset", "A3_PUSH"),  # = touche T
    ("spaceship_targeting", "v_auto_targeting_toggle_long", "A3_PUSH"),           # = T maintenu
    ("spaceship_targeting_advanced", "v_target_cycle_hostile_fwd", "A3_UP"),      # = touche 5
    ("spaceship_targeting_advanced", "v_target_cycle_hostile_reset", "A3_UP"),
    ("spaceship_targeting_advanced", "v_target_cycle_attacker_fwd", "A3_DOWN"),   # = touche 4
    ("spaceship_targeting_advanced", "v_target_cycle_attacker_reset", "A3_DOWN"),
    ("spaceship_targeting_advanced", "v_target_cycle_subitem_fwd", "A3_RIGHT"),   # = touche R
    ("spaceship_targeting", "v_target_unlock", "A3_LEFT"),                        # = Alt gauche + T
    # boutons 6/7 étaient pris par défaut par le mode interaction (F) : on les libère
    ("player_choice", "pc_interaction_mode", None),
    ("player_choice", "pc_focus", None),

    # --- A4 (chapeau haut droit) : modes de vol
    ("spaceship_movement", "v_master_mode_cycle_long", "A4_UP"),        # NAV <-> SCM (maintenir, = B)
    ("spaceship_movement", "v_toggle_landing_system", "A4_RIGHT"),      # train (tap)
    ("spaceship_movement", "v_autoland", "A4_RIGHT"),                   # atterrissage auto (maintenir)
    ("seat_general", "v_toggle_quantum_mode", "A4_DOWN"),
    ("seat_general", "v_toggle_scan_mode", "A4_LEFT"),                  # = V
    ("spaceship_movement", "v_ifcs_vector_decoupling_toggle", "A4_PUSH"),  # = C

    # --- C1 (chapeau latéral pouce) : répartition d'énergie + visée de précision
    ("spaceship_power", "v_engineering_assignment_weapons_increase", "C1_UP"),   # = F5
    ("spaceship_power", "v_engineering_assignment_weapons_max", "C1_UP"),
    ("spaceship_power", "v_engineering_assignment_shields_increase", "C1_RIGHT"),  # = F7
    ("spaceship_power", "v_engineering_assignment_shields_max", "C1_RIGHT"),
    ("spaceship_power", "v_engineering_assignment_reset", "C1_DOWN"),             # = F8
    ("spaceship_power", "v_engineering_assignment_engine_increase", "C1_LEFT"),   # = F6
    ("spaceship_power", "v_engineering_assignment_engine_max", "C1_LEFT"),
    ("spaceship_view", "v_ads_toggle", "C1_PUSH"),                                # = clic droit

    # --- Levier rapid fire : contre-mesures
    ("spaceship_defensive", "v_weapon_countermeasure_decoy_launch", "RF_UP"),   # leurres = H
    ("spaceship_defensive", "v_weapon_countermeasure_noise_launch", "RF_DOWN"),  # bruit = J

    # --- A1 (mini-stick en mode chapeau) : translations
    ("spaceship_movement", "v_strafe_up", "A1_UP"),
    ("spaceship_movement", "v_strafe_down", "A1_DOWN"),
    ("spaceship_movement", "v_strafe_left", "A1_LEFT"),
    ("spaceship_movement", "v_strafe_right", "A1_RIGHT"),

    # --- EN1 (encodeur) : "+ / -" du mode actif
    ("spaceship_weapons", "v_weapon_preset_next", "EN1_A"),
    ("spaceship_weapons", "v_weapon_preset_prev", "EN1_B"),
    ("spaceship_missiles", "v_weapon_increase_max_missiles", "EN1_A"),
    ("spaceship_missiles", "v_weapon_decrease_max_missiles", "EN1_B"),
    ("spaceship_mining", "v_increase_mining_throttle", "EN1_A"),
    ("spaceship_mining", "v_decrease_mining_throttle", "EN1_B"),
    ("spaceship_scanning", "v_inc_scan_focus_level", "EN1_A"),
    ("spaceship_scanning", "v_dec_scan_focus_level", "EN1_B"),

    # --- SW1 (interrupteur du socle)
    ("spaceship_general", "v_flightready", "SW1_UP"),
    ("vehicle_general", "v_flightready", "SW1_UP"),
    ("spaceship_movement", "v_atc_request", "SW1_DOWN"),

    # --- F1 / F2 / F3 (boutons du socle)
    ("lights_controller", "v_lights", "F1"),
    ("spaceship_general", "v_toggle_all_doors", "F2"),
    ("vehicle_general", "v_toggle_all_doors", "F2"),
    ("spaceship_movement", "v_vtol_toggle", "F3"),
]

# Ordre des actionmaps = ordre du defaultProfile.xml du jeu (4.10)
MAP_ORDER = [
    "seat_general", "spaceship_general", "spaceship_view", "spaceship_movement", "spaceship_quantum",
    "spaceship_targeting", "spaceship_targeting_advanced", "spaceship_scanning", "spaceship_mining",
    "spaceship_salvage", "spaceship_weapons", "spaceship_missiles", "spaceship_defensive", "spaceship_power",
    "lights_controller", "vehicle_general", "vehicle_driver", "player_choice",
]
MAP_CATEGORY = {
    "seat_general": "@ui_CCSeatGeneral", "spaceship_quantum": "@ui_CCSeatGeneral",
    "lights_controller": "@ui_CGLightControllerDesc", "vehicle_general": "@ui_CCVehicle",
    "vehicle_driver": "@ui_CCVehicle", "player_choice": "@ui_CGInteraction",
}


def rebind_input(control):
    if control is None:
        return f"{JS}_ "
    return f"{JS}_{BUTTONS[control]}"


def build_xml():
    by_map = {}
    for amap, action, control in BINDINGS:
        by_map.setdefault(amap, {}).setdefault(action, []).append(rebind_input(control))
    unknown = set(by_map) - set(MAP_ORDER)
    if unknown:
        sys.exit(f"actionmap(s) absente(s) de MAP_ORDER : {sorted(unknown)}")

    out = [f'<ActionMaps version="1" optionsVersion="2" rebindVersion="2" profileName="{PROFILE_NAME}">',
           f' <CustomisationUIHeader label="{PROFILE_NAME}" description="" image="">',
           '  <devices>', '   <keyboard instance="1"/>', '   <mouse instance="1"/>',
           '   <joystick instance="1"/>', '  </devices>', '  <categories>']
    cats = []
    for m in MAP_ORDER:
        if m in by_map:
            c = MAP_CATEGORY.get(m, "@ui_CCSpaceFlight")
            if c not in cats:
                cats.append(c)
    out += [f'   <category label="{c}"/>' for c in cats]
    out += ['  </categories>', ' </CustomisationUIHeader>',
            ' <options type="keyboard" instance="1" Product="Keyboard  {6F1D2B61-D5A0-11CF-BFC7-444553540000}"/>',
            f' <options type="joystick" instance="1" Product="{PRODUCT}"/>',
            ' <modifiers />']
    for m in MAP_ORDER:
        if m not in by_map:
            continue
        out.append(f' <actionmap name="{m}">')
        for action in sorted(by_map[m]):
            out.append(f'  <action name="{action}">')
            for inp in dict.fromkeys(by_map[m][action]):
                out.append(f'   <rebind input="{inp}"/>')
            out.append('  </action>')
        out.append(' </actionmap>')
    out.append('</ActionMaps>')
    return "\n".join(out) + "\n"


def check(default_profile):
    root = ET.parse(default_profile).getroot()
    defaults = {}
    for am in root.iter("actionmap"):
        for a in am.findall("action"):
            js = (a.get("joystick") or "").strip()
            sub = a.find("joystick")
            if not js and sub is not None:
                js = (sub.get("input") or "").strip()
            defaults[(am.get("name"), a.get("name"))] = js
    ok = True
    for amap, action, _ in BINDINGS:
        if (amap, action) not in defaults:
            print(f"INCONNU : {amap}/{action}")
            ok = False
    # assignations effectives = défauts du jeu, remplacés par nos rebinds
    effective = {k: ([v] if v else []) for k, v in defaults.items()}
    for (amap, action) in {(m, a) for m, a, _ in BINDINGS}:
        effective[(amap, action)] = [BUTTONS[c] for m, a, c in BINDINGS if (m, a) == (amap, action) and c]
    used = {}
    for (amap, action), inputs in effective.items():
        for inp in inputs:
            used.setdefault(inp, []).append(f"{amap}/{action}")
    print("\nAssignations joystick effectives après import :")
    for inp in sorted(used, key=lambda s: (not s.startswith("button"), int(s[6:]) if s.startswith("button") and s[6:].isdigit() else 0, s)):
        print(f"  js1_{inp:12s} {', '.join(sorted(used[inp]))}")
    return ok


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", metavar="defaultProfile.xml")
    ap.add_argument("--out", default=os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                                  f"layout_{PROFILE_NAME}_exported.xml"))
    args = ap.parse_args()
    if args.check and not check(args.check):
        sys.exit(1)
    xml = build_xml()
    ET.fromstring(xml)  # doit être du XML valide
    with open(args.out, "w", encoding="utf-8", newline="\r\n") as f:
        f.write(xml)
    print(f"\nÉcrit : {args.out}")


if __name__ == "__main__":
    main()
