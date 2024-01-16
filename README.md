** ✨Huntastic✨ **

**Description** Chaque joueur.euse a un rôle : une poule, un renard ou une vipère. Chasse sa proie, évite son prédateur, et libère ses coéquipier.es emprisonné.es.
  
**🎯 Contexte & cahier des charges** : développé dans le cadre du cours de programmation avancée.

**🎲 Règles du jeu** : maquette, déroulé d'une partie, conditions de victoire
      **Maquette "Poule, Renard, Vipère"**

  Déroulé d'une Partie
  
  1. **Attribution des Rôles :**
     - Chaque joueur.euse est assigné à l'un des trois rôles : Poule, Renard, ou Vipère.
     - Les rôles définissent les interactions et les objectifs du.de la joueur.euse.
  
  2. **Chasse et Capture :**
     - Les Poules chassent les Renards, les Renards chassent les Vipères, et les Vipères chassent les Poules.
     - Les joueurs peuvent capturer leur proie en effectuant des actions spécifiques.
  
  3. **Libération et Réapparition :**
     - Les joueurs ont le pouvoir de libérer leurs coéquipiers capturés.
     - En cas d'élimination par leur proie, les joueurs réapparaissent instantanément à leur base.
  
  4. **Évasion de la Zone de Prison :**
     - Les Poules, Renards et Vipères ont la capacité de libérer leurs compatriotes de la zone de prison.
  
  5. **Combat Corps à Corps :**
     - Les joueur.euses attaquant.es ne subissent pas de dégâts au corps à corps.
     - Les joueur.euses chassé.es prennent des dégâts lors des confrontations rapprochées.
  
  6. **Immunité au sein de l'Équipe :**
     - Les membres de l'équipe ne se font pas de mal entre eux, favorisant la coopération.
  
   Conditions de Victoire
  
  - **Atteindre l'Objectif d'Équipe :**
     - La victoire est déterminée par l'accomplissement d'objectifs spécifiques définis par l'équipe.
     - Coopérez stratégiquement pour éliminer les membres de l'équipe adverse et atteindre les conditions de victoire.

** Ressources ** 
  - background généré avec l'IA de Canva. 



**🎮 Use cases**: 
    - pour l'administrateur.rice : L'administrateur.rice peut ajouter des fonctions ou les modifier à partir du fichier fonction pour y chanegr des règles. Iel peut également modifier les règles de l'arène depuis le fichier rules.json
    - 
    - pour le.a joueur.euse : README_api
    - 


**🧪 Tests**: 
    **1. Affectation du rôle :**
   - Vérifier que l'utilisateur.rice peut choisir un rôle parmi poule, renard, et vipère.
   - Assurer que le rôle attribué est correctement affiché dans l'interface utilisateur.rice.

   **2. Interaction entre les rôles :**
  - En tant que poule/ renard / vipère  vérifier que l'utilisateur.rice peut être attrapé.e par les renards.
  - Vérifier que les interactions entre les rôles respectent les règles du jeu.
    
   **3. Libération des coéquipiers :**
  - En tant que poule/renard/vipère, vérifier que l'utilisateur.rice peut libérer les poules/renards/vipères.
  - Vérifier que la libération est correctement enregistrée dans le système.
    
   **4. Réapparition après la mort :**
  - Vérifier que, en tant que poule/renard/vipère, si l'utilisateur.rice est tué.e par sa proie, il réapparaît immédiatement à sa base.
  - Assurer que la réapparition se fait de manière fluide et sans erreurs.
    
   **5. Libération des coéquipiers de la zone de prison :**
  - En tant que poule/renard/vipère, vérifier que l'utilisateur.rice peut libérer ses coéquipiers de la zone de prison.
  - S'assurer que la libération est correctement enregistrée dans le système.
    
   **6. Gestion des dégâts :**
  - En tant que joueur.euse attaquant.e, vérifier qu'aucun dégât n'est reçu au corps à corps.
  - En tant que joueur.euse chassé.e, vérifier que des dégâts sont reçus au corps à corps.
  - Assurer que la capture se produit correctement en cas de dégâts au corps à corps.
    
   **7. Immunité entre membres de l'équipe :**
  - En tant que joueur.euse, vérifier qu'aucun dégât n'est reçu de la part des autres membres de l'équipe.
  - Assurer que les membres de l'équipe ne peuvent pas se causer de dommages entre eux.
    	 
   **8. Tests de documentation :**
  - Vérifier que la documentation du jeu est à jour et qu'elle décrit correctement les différentes fonctionnalités et règles du jeu.
    
    

**🧑‍💻 Auteur.rices** Thanina GUERNINE, Hugo LE COUPANEC, Eva POTTIER


