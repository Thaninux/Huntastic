        import time
        import random
        import json

        #création de l'arene et des regles
        def createRules(agent):
          
          agent.ruleArena("info", "⌛ Initialisation de l'agent...")
          while ( len(agent.game) == 0 ):
            agent.lookAt((agent.dir+1)%4)
            agent.update()
            time.sleep(0.5)

          agent.ruleArena("reset", True)
          agent.update()
          time.sleep(1)
          with open(os.path.join("./", 'regles.json'),'r' , encoding='utf-8') as json_data:
            regles_arena = json.load(json_data)
          
            for regle in regles_arena["rules"]:
              nom_regle = regle["name"]
              valeur_regle = regle["value"]

      # Appeler la fonction agent.ruleArena avec les clés et les valeurs
      agent.ruleArena(nom_regle, valeur_regle)

          agent.update()

          time.sleep(1)

        def playerAppeared(agentState, playerId, agent, teams):
          """
          :agentState: Etat du joueur
          :playerId: Id du joueur
          :agent: agent
          :teams: Equipes
          Gère l'arrivée d'un joueur et son placement dans une équipe
          """
            agentState[playerId] = {}
            agentState[playerId]['state'] = 0
            agentState[playerId]['playerId'] = playerId
            team=0
            profile=0
            x=0
            y=0
            match teams.index(min(teams)):
                case(0):
                    teams[0] += 1
                    team = 0
                    profile = 0
                    x = 25
                    y = 0
                case(1):
                    teams[1] += 1
                    team = 1
                    profile = 2
                    x = 47
                    y = 47
                case(2):
                    teams[2] += 1
                    team = 2
                    profile = 3
                    x = 2
                    y = 47
            agent.rulePlayer(playerId,"profile", profile)
            agent.rulePlayer(playerId,"team", team)
            agent.rulePlayer(playerId,"x", x)
            agent.rulePlayer(playerId,"y", y)
            agentState[playerId]['team'] = team

        def playerLeft(before, agentState, teams):
          """
          :before:
          :agentState: Etat de l'agent (prison ou non)
          :teams: Liste des joueurs d'une équipe
          Cette fonction sert à gérer lorsque qu'un joueur quitte la partie."""
            for agentId in before:
                disappeared = True
                for playerN in agentState.keys():
                    if(disappeared):
                        if(agentId == playerN):
                            disappeared = False
                if(disappeared):
                    teams[agentState[agentId]["team"]]-=1

        def playerAttack(agent, agentState):
          """
          :agent: L'agent
          :agentState: Etat de l'agent (prison ou non)
          Gère l'attaque entre deux agents
          """
            for predator in agentState:
                for prey in agentState:
                    if(agentState[predator]["team"] == (agentState[prey]["team"] +1) % 3):
                        if(agentState[predator]["x"] <= agentState[prey]["x"]+1 and
                           agentState[predator]["x"] >= agentState[prey]["x"]-1 and
                           agentState[predator]["y"] <= agentState[prey]["y"]+1 and
                           agentState[predator]["y"] >= agentState[prey]["y"]-1):
                            if(agentState[prey]["state"] == 0):
                                agentState[prey]["life"]-=1
                                if(agentState[prey]["life"] == 0):
                                    agentState[prey]["life"] = 2
                                    agentState[prey]["state"] = 1
                                    agentState[prey]["killedBy"] = agentState[predator]["playerId"]
                                agent.rulePlayer(agentState[prey]["playerId"], "life", agentState[prey]["life"]-1)



        def free(team, agent, agentState):
          """
          :team: Equipe de l'agent
          :agent: l'agent
          :agentState: état de l'agent (prison ou non)
          Prend en paramètre l'id de la team et procède à la libération de tous les membres en prison"""
          for playerId in agent.range.keys():
              if agentState[playerId]['team'] == team and agentState[playerId]['state'] == 1:
                  agentState['state'] = 0

        def getJailPosition(agent):
          """
          :agent: l'agent
          Renvoie les positions (x,y) des prisons dans un dictionnaire"""
          l = {'Jail0':[],'Jail1':[],'Jail2':[]}
          for x in range(len(agent.map)):
              for y in range(len(agent.map[0])):
                  if agent.map[x][y] == 1:
                      l["Jail0"].append((x,y))
                  elif agent.map[x][y] == 2:
                      l["Jail1"].append((x,y))
                  elif agent.map[x][y] == 3:
                      l["Jail2"].append((x,y))
          return l

        def keepInJail(playerId, agent, agentState, jails):
          """
          :playerId: Id du joueur
          :agent: l'agent
          :agentState: Etat de l'agent (prison ou non)
          :jails: Coordonnées des prisons
          Vérifie si le joueur est en prison et si oui, le garde dans la prison
          """
          team = agentState[playerId]["team"]
          jail = "Jail" + str(team)
          #print(jails["Jail0"])
          #print((agentState[playerId]['x'],agentState[playerId]['y']) not in jails[jail])
          if (agentState[playerId]['x'],agentState[playerId]['y']) not in jails[jail] :
              n = random.randint(0,len(jails[jail])-1)
              agentState[playerId]['x'] = jails[jail][n][0]
              agentState[playerId]['y'] = jails[jail][n][1]
              print(jails[jail][n])
              agent.rulePlayer(playerId,'x',jails[jail][n][0])
              agent.rulePlayer(playerId,'y',jails[jail][n][1])

        def 