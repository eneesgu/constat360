# VKB Gladiator NXT EVO (main droite) : profil Star Citizen

Profil prêt à importer pour **Star Citizen 4.10.2** (version LIVE du 7 octobre 2026), avec un **VKB Gladiator NXT EVO, main droite, grip SCG**, sur le **profil d'usine VKB**. Le clavier reste à gauche (ZQSD/WASD, etc.).

- Fichier à importer : [`layout_VKB_NXT_EVO_R_FR_exported.xml`](layout_VKB_NXT_EVO_R_FR_exported.xml)
- Pour régénérer après modification : `python3 generate_layout.py` (la table `BINDINGS` est la seule chose à éditer)

---

## 1. Toutes les commandes de la manette

Numéros = numérotation DirectInput du profil d'usine VKB (ce que Star Citizen affiche sous la forme `js1_buttonX`).

| Étiquette | Type | Où | Numéros |
|---|---|---|---|
| Gâchette | 2 crans | index | 1er cran = **1**, 2e cran = **2** |
| **A2** | gros bouton rouge | tête, en bas à gauche | **3** |
| **B1** | bouton | avant de la tête, sous l'index (au-dessus du levier rapid fire) | **4** |
| **D1** | bouton | bas de la poignée, petit doigt | **5** |
| **A3** | chapeau 4 directions + clic | tête, **au milieu** | haut 6, droite 7, bas 8, gauche 9, clic **10** |
| **A4** | chapeau 4 directions + clic | tête, en haut à droite | haut 11, droite 12, bas 13, gauche 14, clic 15 |
| **C1** | chapeau 4 directions + clic | côté de la poignée, sous le pouce | haut 16, droite 17, bas 18, gauche 19, clic 20 |
| Rapid fire | levier haut / bas | sous B1, index | haut 21, bas 22 |
| **A1** | mini-stick (mode chapeau) | tête, en haut à gauche | chapeau `hat1` ; le clic bascule chapeau ↔ analogique (réglage VKB) |
| **EN1** | encodeur rotatif (molette crantée) | socle, à droite | un sens 23, l'autre 24 |
| **SW1** | interrupteur à rappel 3 positions | socle, à gauche | haut 25, bas 26 |
| **F1 / F2 / F3** | boutons | dessus du socle (ordre physique : F2, F1, F3) | F1 27, F2 28, F3 29 |
| Molette des gaz | axe analogique | socle, **au milieu** | axe `z` |
| Manche | axes | — | X = `x`, Y = `y`, torsion = `rotz` |

## 2. Pourquoi « ça ne fait plus ce que ça faisait avant »

Star Citizen met des actions joystick **par défaut** sur les boutons 1 à 12. Après une mise à jour ou une remise à zéro des commandes, elles reviennent et entrent en conflit avec tes réglages. Sur ton VKB, ça donne :

| Bouton | Ce que le jeu y met par défaut (4.10) |
|---|---|
| **A3 clic** (10) | **Translation vers le bas** : c'est pour ça que le ciblage sur A3 ne marchait pas |
| A3 haut (6) | Mode interaction (touche F) |
| A3 bas (8) | Boost |
| A3 gauche (9) | Translation vers le haut |
| **A2 rouge** (3) | Leurres + angle de scan + puissance laser de minage |
| B1 (4) | Angle de scan / puissance de minage (moins) |
| D1 (5) | Contre-mesure bruit |
| Gâchette 2e cran (2) | Missile suivant (donc tu changeais de missile en appuyant à fond) |
| A4 droite (12) | Train d'atterrissage |

Le profil ci-dessous réassigne ou efface **tous** ces conflits.

## 3. Ce que je configure (proposition, à valider)

« Selon le mode » = l'action dépend du mode opérateur actif (canons, missiles, minage, scan, quantum), exactement comme le clic gauche ou la molette de la souris dans le jeu.

### Gâchette et index
| Commande | Action | Équivalent clavier/souris | Alternatives possibles |
|---|---|---|---|
| Gâchette 1er cran | Tirer (canons) · lancer missiles (mode missiles) · sauter en quantum, maintenir (mode quantum) · scanner (mode scan) · laser de minage · récupération | clic gauche | — |
| Gâchette 2e cran | **Rien** (libéré) | — | Tirer le groupe d'armes 2 · visée de précision maintenue |
| Rapid fire haut | **Leurres** (appui = salve, maintien = régler la salve) | H | Missile suivant |
| Rapid fire bas | **Bruit** (paillettes) | J | Nombre de missiles armés + |
| **B1** | Canons : **verrouiller/déverrouiller le cardan** · Missiles : **type de missile suivant** · Minage : changer de laser | G / molette / Alt+clic | Visée de précision (clic droit) |

### Tête du manche (pouce)
| Commande | Action | Équivalent | Alternatives |
|---|---|---|---|
| **A2 rouge** | **Mode missiles on/off** (comme tu l'avais) | — | Mode opérateur suivant (clic molette) |
| **A3 clic** | **Cibler** : comme la touche T (appui = cible sous le réticule/cible suivante en vue, maintenu = ciblage auto on/off) | T | Uniquement « verrouiller la cible sous le réticule » |
| A3 haut | Ennemi suivant | 5 | Épingler la cible |
| A3 bas | Attaquant suivant (qui te tire dessus) | 4 | Allié suivant |
| A3 droite | Sous-cible suivante (composants) | R | Cible suivante en vue |
| A3 gauche | Déverrouiller la cible | Alt gauche + T | Sous-cible précédente |
| A4 haut | **NAV ↔ SCM** (maintenir ~¼ s) | B maintenu | — |
| A4 droite | Train (appui) / atterrissage auto (maintien) | N | — |
| A4 bas | Mode quantum (puis maintenir la gâchette pour sauter) | — | Carte stellaire |
| A4 gauche | Mode scan | V | Ping radar (Tab) |
| A4 clic | Mode découplé | C | Frein spatial (X) |
| C1 haut | Énergie **armes** + (maintien = max) | F5 | — |
| C1 droite | Énergie **boucliers** + (maintien = max) | F7 | — |
| C1 gauche | Énergie **moteurs** + (maintien = max) | F6 | — |
| C1 bas | Réinitialiser la répartition d'énergie | F8 | Frein spatial |
| C1 clic | **Visée de précision** (zoom) on/off | clic droit | Verrou cardan |
| A1 mini-stick | Translations haut / bas / gauche / droite | Espace / Ctrl / Q / D | En mode analogique : translations proportionnelles |
| **D1** (petit doigt) | **Boost** (maintenir) | Shift gauche | Frein spatial |

### Socle
| Commande | Action | Équivalent | Alternatives |
|---|---|---|---|
| Molette des gaz (milieu) | **Limiteur de vitesse** (absolu) | Alt + molette | Gaz avant/arrière · rien |
| EN1 | « + / − » du mode actif : preset d'armes (canons) · nombre de missiles armés (missiles) · puissance laser (minage) · angle de scan (scan) | molette souris / G | Zoom |
| SW1 haut | Prêt au vol (démarrage) | Alt droite + R | Allumer/éteindre tout (U) |
| SW1 bas | Demander l'atterrissage | Alt gauche + N | Ouvrir/fermer les portes |
| F1 | Phares | L | — |
| F2 | Ouvrir/fermer toutes les portes | (aucune par défaut) | Verrouiller les portes |
| F3 | VTOL | K | Carte stellaire (F2) |

### Axes
- Manche gauche/droite = **lacet** (yaw), avant/arrière = **tangage** (pitch), **torsion = roulis** (roll) : réglage par défaut du jeu.
- Alternative très répandue : gauche/droite = roulis et torsion = lacet. Dis-le-moi et j'inverse.

## 4. Installation

1. **Ferme Star Citizen.**
2. **Sauvegarde** ton fichier actuel : `C:\Program Files\Roberts Space Industries\StarCitizen\LIVE\user\client\0\Profiles\default\actionmaps.xml` (copie-le ailleurs).
3. Copie `layout_VKB_NXT_EVO_R_FR_exported.xml` dans
   `C:\Program Files\Roberts Space Industries\StarCitizen\LIVE\user\client\0\Controls\Mappings\`
   (crée le dossier `Mappings` s'il n'existe pas ; adapte le chemin si le jeu est installé ailleurs).
4. Lance le jeu → **Options → Keybindings (Commandes) → Advanced Controls Customization → Control Profiles** → choisis `VKB_NXT_EVO_R_FR` → importe-le (si le jeu te demande quels périphériques importer, coche le joystick).
   Autre méthode : console (touche `²`/`~`) → `pp_rebindkeys layout_VKB_NXT_EVO_R_FR_exported`
5. Si tu as **plusieurs joysticks / volants / pédales branchés**, le VKB n'est peut-être pas `js1`. Vérifie dans l'écran des commandes : clique sur une action et appuie sur la gâchette ; si le jeu affiche `js2_button1`, dis-le-moi et je régénère le fichier pour `js2`.

## 5. Réglages à vérifier

- **VKBDevCfg** (logiciel VKB) : ton manche doit être sur le **profil d'usine**. Si tu avais bricolé quelque chose dedans (« la magouille »), les numéros peuvent être différents.
- **Vérifier les numéros** : Windows → `Win + R` → `joy.cpl` → Propriétés : appuie sur chaque bouton et note le numéro qui s'allume. S'il ne correspond pas au tableau de la section 1, envoie-moi les numéros.
- **Molette des gaz** : si ton vaisseau est très lent, tourne la molette vers le haut (c'est le limiteur de vitesse). Si elle marche à l'envers : Options → Keybindings → Advanced Controls Customization → réglages du joystick → inverser l'axe du limiteur.
- **EN1** : si « + » et « − » sont inversés, dis-le-moi, j'inverse 23 et 24.
- **Zones mortes** : avec un VKB neuf, aucune n'est nécessaire. Si le vaisseau dérive au repos, mets une petite zone morte (2-3 %) sur X/Y dans les réglages du joystick du jeu.

## Sources

- Schéma et numérotation du NXT EVO R : [BindSight (w00zla)](https://github.com/w00zla/BindSight), [sc-mapper (hamlet2k)](https://github.com/hamlet2k/sc-mapper), [diagramme VKB du projet x4_vkb](https://github.com/codejnki/x4_vkb), [modèle NXT Premium (franklesniak)](https://github.com/franklesniak/HOTAS-HOSAS_Control_Mapping_Template_Files), forum VKB ([A2 = bouton 3, SW1 haut = 25](http://forum.vkb-sim.pro/viewtopic.php?t=7523), [SW1/EN1](http://forum.vkb-sim.pro/viewtopic.php?t=8338))
- Actions et assignations par défaut du jeu : `defaultProfile.xml` de Star Citizen 4.10.2 (build 4.10.196.36804), via [sc-mapper](https://github.com/hamlet2k/sc-mapper/tree/main/data/game)
- Composition du socle EVO (3 boutons, interrupteur 3 positions, molette des gaz, encodeur) : [fiche VIP Pilot](https://vippilot.com/products/gladiator-nxt-evo-base-only/), [test PC Gamer](https://www.pcgamer.com/hardware/controllers/vkb-gladiator-nxt-evo-f-14-combat-edition-stecs-throttle-system-review/)
