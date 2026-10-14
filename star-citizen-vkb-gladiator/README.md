# VKB Gladiator NXT EVO (main droite) : profil Star Citizen

Profil pour **Star Citizen 4.10.2** (LIVE du 7 octobre 2026), **VKB Gladiator NXT EVO main droite, grip SCG, profil d'usine VKB**. Le clavier reste à gauche.

Chaque commande a un rôle, et pour chacune il existe une liste d'options cohérentes (208 au total), toutes vérifiées une par une dans le `defaultProfile.xml` du jeu :

| Fichier | À quoi il sert |
|---|---|
| `layout_VKB_NXT_EVO_R_FR_exported.xml` | le profil à importer dans le jeu (recommandations par défaut) |
| `options.json` | toutes les options de chaque commande, avec la recommandation |
| `choices.json` (facultatif) | tes choix quand ils diffèrent de la recommandation, ex. `{"D1": "vue_libre"}` ; `"none"` = laisser vide |
| `generate_layout.py` | refait le profil à partir des deux fichiers ci-dessus : `python3 generate_layout.py` |

## La disposition recommandée

### Tête du manche (pouce)
| Commande | Rôle | Action recommandée | Clavier |
|---|---|---|---|
| **A2** rouge | Cibler | Appui court : verrouille la cible sous le réticule, le rond de tir apparaît · appui long : ciblage auto on/off | T |
| **A3** clic | Scanner | Mode scan on/off | V |
| A3 haut | | Onde radar (ping), maintenir puis relâcher | Tab |
| A3 droite | | Ennemi le plus proche, puis suivant | 5 |
| A3 gauche | | Tous les contacts détectés, un par un | 7 |
| A3 bas | | Composant suivant de la cible | R |
| **A1** haut | Armes | Mode canons (lasers / balistiques) | |
| A1 bas | | Mode missiles / bombes | |
| A1 droite / gauche | | Suivant / précédent selon le mode : groupe d'armes, type de missile ou de bombe, cône de scan, puissance du laser de minage | molette souris |
| **A4** clic | Quantum et boucliers | NAV ↔ SCM (maintenir ¼ s) : en NAV, boucliers et armes coupés, quantum disponible | B maintenu |
| A4 haut | | Mode quantum on/off (puis gâchette maintenue = saut) | |
| A4 bas | | Boucliers on/off | O |
| A4 droite / gauche | | Énergie boucliers / armes +1 (maintenir = max) | F7 / F5 |
| **C1** clic | Atterrissage | Appui court : demande à la tour · maintenir : atterrissage auto | Alt+N / N maintenu |
| C1 haut | | VTOL on/off | K |
| C1 bas | | Mode précision auto on/off | |
| C1 gauche | | Amarrage (court) / caméra d'amarrage (maintenu) | Alt Gr+N / 0 |
| C1 droite | | Demande de zone de chargement | Alt Gr+N |

### Index et petit doigt
| Commande | Action recommandée | Clavier |
|---|---|---|
| Gâchette, 1er cran | Tir, ou action du mode actif (missile, saut quantique maintenu, scan, minage, récupération) | clic gauche |
| Gâchette, 2e cran | Ajoute le groupe d'armes 2 (ex. lasers en groupe 1, balistiques en groupe 2) | |
| **B1** | Boost, tant qu'on appuie | Shift gauche |
| Rapid fire haut / bas | Leurres / bruit | H / J |
| **D1** | Frein spatial, tant qu'on appuie | X |

### Socle
| Commande | Action recommandée | Clavier |
|---|---|---|
| **F1** | Train d'atterrissage sortir / rentrer | N |
| **F2** | HUD avancé on/off (cockpit plus détaillé) | aucune |
| **F3** | Prêt au vol (démarrer le vaisseau) | Alt Gr+R |
| **SW1** haut / bas | Fermer / ouvrir toutes les portes | aucune |
| Molette du milieu | Limiteur de vitesse (en bas = lent, en haut = plein régime) | Alt+molette |
| **EN1** | Limiteur d'accélération + / − | Alt Gr+molette |

### Axes
| Axe | Action |
|---|---|
| X : incliner gauche / droite | **Roulis** : incliner à droite = le vaisseau s'incline à droite |
| Y : pousser / tirer | Tangage : pousser = piquer, tirer = cabrer |
| Rz : torsion de la poignée | Lacet : le nez tourne à droite / à gauche |
| Rx / Ry : mini-stick A1 en mode analogique | Translations gauche/droite et haut/bas (clic sur A1 pour passer en analogique ; re-clic pour revenir aux armes) |

Si un axe part dans le mauvais sens, il existe une option « sens inversé » pour chacun.

## Changer une commande

Ouvre la page interactive (`profil-gladiator.html`, ou le lien que je t'ai donné), choisis dans le menu de chaque direction, puis **Copier mes choix** et colle le texte dans la conversation : je refais le profil. La page prévient si une même action se retrouve sur deux boutons, ce que le jeu n'accepte pas.

## Tester hors jeu

1. **Testeur de la page** : ouvre `profil-gladiator.html` sur ton PC avec Chrome ou Edge, clique sur « Démarrer le test », appuie sur chaque bouton. La page affiche le nom du bouton (ex. « A3 · clic »), son numéro et l'action qu'il fera. Chaque bouton testé passe au vert, et les barres des 6 axes bougent avec le manche.
2. **Sans rien installer** : Win + R → `joy.cpl` → VKB → Propriétés. Vérifie que les numéros correspondent : gâchette 1 et 2, A2 = 3, B1 = 4, D1 = 5, A3 = 6 à 10 (clic = 10), A4 = 11 à 15, C1 = 16 à 20, rapid fire = 21/22, EN1 = 23/24, SW1 = 25/26, F1 = 27, F2 = 28, F3 = 29, A1 = chapeau (POV).
3. **Le profil lui-même** ne peut être vraiment testé qu'en jeu. Après l'import, l'écran des commandes affiche `js1_button10` à côté de « Toggle Scanning Operator Mode », etc.

Si un numéro ne correspond pas, envoie-le-moi : ta manette n'est alors pas sur la numérotation d'usine, et j'adapte le profil.

## Installation

1. Ferme le jeu. Sauvegarde `...\StarCitizen\LIVE\user\client\0\Profiles\default\actionmaps.xml`.
2. Copie `layout_VKB_NXT_EVO_R_FR_exported.xml` dans `...\StarCitizen\LIVE\user\client\0\Controls\Mappings\`.
3. En jeu : Options → Keybindings → Advanced Controls Customization → Control Profiles → `VKB_NXT_EVO_R_FR` → importer (cocher le joystick).
   Ou console : `pp_rebindkeys layout_VKB_NXT_EVO_R_FR_exported`
4. Plusieurs joysticks branchés ? Si le jeu affiche `js2_…` pour la gâchette, le profil doit être refait pour js2.

Le profil efface tout seul les actions joystick que le jeu met par défaut sur ces boutons (translations sur A3, leurres sur A2, boost, mode interaction, réglages de minage et de scan), pour que chaque bouton ne fasse que ce qui est prévu.

## Points à confirmer en jeu

- Le HUD avancé (F2) est la meilleure piste pour le « cockpit plus détaillé », mais son affichage exact en 4.10 n'a pas pu être vérifié.
- Bombes : dans les fichiers 4.10, elles passent par le mode missiles (A1 bas). Ça dépend du vaisseau.
- En NAV, les guides 4.10 disent que boucliers et armes sont coupés. Selon le patch, le mode quantum peut déjà être actif en NAV.
- EN1 : on ne sait pas quel sens physique envoie 23 ou 24. Si c'est inversé, dis-le.

## Sources

- Actions, assignations par défaut et réglages des axes : `defaultProfile.xml` de Star Citizen 4.10.2 (build 4.10.196.36804), via [sc-mapper](https://github.com/hamlet2k/sc-mapper/tree/main/data/game)
- Numérotation du NXT EVO R : [BindSight](https://github.com/w00zla/BindSight), [diagramme VKB (x4_vkb)](https://github.com/codejnki/x4_vkb), [modèle NXT Premium](https://github.com/franklesniak/HOTAS-HOSAS_Control_Mapping_Template_Files), forum VKB ([A2 = 3, SW1 = 25](http://forum.vkb-sim.pro/viewtopic.php?t=7523), [SW1/EN1](http://forum.vkb-sim.pro/viewtopic.php?t=8338))
- Socle EVO (3 boutons, interrupteur 3 positions, molette, encodeur) : [VIP Pilot](https://vippilot.com/products/gladiator-nxt-evo-base-only/), [PC Gamer](https://www.pcgamer.com/hardware/controllers/vkb-gladiator-nxt-evo-f-14-combat-edition-stecs-throttle-system-review/)
- Liste des commandes 4.10 (HUD avancé, mode précision) : [scfocus.org](https://scfocus.org/star-citizen-key-bindings/)
