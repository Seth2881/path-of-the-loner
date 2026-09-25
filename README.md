# PROJET PATH OF THE LONER

membre du groupe : 
    Paquet-Deom Pierre

voir conception_structure_jeu.txt pour les spécifications d'effets

## Organisation :

Le projet est ogranisé en deux dossiers et un fichier main.py :
    -| un dossier data avec quatres fichiers json contenant les différentes armes, monstres, armures et ascendances
    -| un dossier classes avec quatre fichiers :
        -| arena.py qui gère la classe arena, le combat contre un bot joueur
        -| monster.py qui gère les pv et dêgats des différents mobs
        -| player.py qui gère les différents type de joueurs ainsi que les armes et les armures
        -| rooms.py qui choisis le nombre de monstre et les monstres présent dans les différentes pièces
        
## Conception du projet

Le projet suit une architecture simple et "data-driven" pour séparer les données de configuration, la logique métier et l'orchestration :

- Dossier data : fichiers JSON décrivant armes, armures, ascendances et monstres. Chaque entrée contient les propriétés nécessaires (PV, dégâts, effets, type, etc.). Ces fichiers sont chargés au démarrage, ce qui permet d'ajouter ou d'équilibrer du contenu sans modifier le code.
- Dossier classes : implémentation de la logique de jeu
  - player.py : classes Character, Weapon, Armor — gestion des statistiques, des attaques et des effets liés à l'équipement.
  - monster.py : classe Monster — PV, dégâts et comportements spécifiques aux monstres.
  - arena.py : gestion d'un combat PvP (ordre d'attaque, résolution des dégâts, conditions de victoire).
  - rooms.py : génération des rencontres PvE (nombre/type de monstres par salle, progression entre salles).
- main.py : orchestration — chargement des données, création du personnage via l'interface console, choix PvP/PvE et boucle principale du jeu.

Principes de conception :
- Data-driven : contenu et paramètres dans des JSON pour faciliter l'itération.
- Séparation des responsabilités : chaque module a une responsabilité unique et testable.
- Extensibilité : ajouter une arme/armure/monstre = ajouter une entrée JSON ; ajouter un nouveau mécanisme = nouvelle classe intégrée via main.py.
- Scalabilité : l'ajout d'une arme/armure/monstre se fait simplement en ajoutant une entrée JSON ; l'introduction d'un nouveau mécanisme nécessite l'intégration d'une nouvelle classe via la fonction main.
- Testabilité : logique intégrée dans des classes afin de faciliter les tests unitaires.


Améliorations envisageables :
- Regrouper le système d'effets (améliorations/diminutions) pour une meilleure réutilisation.
- Intégrer la fonctionnalité de sauvegarde et de chargement de jeu.
- Intégrer une interface graphique ou une interface texte améliorée.
