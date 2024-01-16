import j2l.pytactx.agent as pytactx
import functions

agent = pytactx.Agent(playerId="",
            arena="huntastic",
            username="",
            password="",
            server="mqtt.jusdeliens.com",
                        port=1883)

#création de l'arene
functions.createRules(agent)

for x in range(20,-1,-1):
    agent.ruleArena("info", "-"+str(x))
    agent.update()

before = []
teams = [0,0,0]
# Affichage dans l'arène du début de la partie par l'agent
agent.ruleArena("info", "🟢 C'est parti !")

agent.update()

#premiere partie des tests permettant de tester les différentes parties du code
"""agents = {
    "joueur1": {
        "x": 0,
        "y": 0,
    },
    "joueur2": {
        "x": 5,
        "y": 7,
    },
    "joueur3": {
        "x": 13,
        "y": 3,
        "life": 0,
    }
}
for agentId, attributes in agents.items():
    for attributeKey, attributeValue in attributes.items():
        agent.rulePlayer(agentId, attributeKey, attributeValue)
"""

#agentState{agentId: {"state": 0||1, "x":x, "y":y, "team":team}}
agentState = {}


#map

jails = functions.getJailPosition(agent)
while True:

    agent.update()

    for agentId in agent.range.keys():
      #Verifie si de nouveaux agents sont apparus dans la partie
        if agentId not in agentState.keys():
            functions.playerAppeared(agentState, agentId, agent, teams)

      #met a jour les donnees des agents
        agentState[agentId]['x'] = agent.range[agentId]["x"]
        agentState[agentId]['y'] = agent.range[agentId]["y"]
        agentState[agentId]['life'] = agent.range[agentId]['life']
        agentState[agentId]['score'] = agent.range[agentId]['score']

    
    #Vérifie si un joueur a quitté la partie
    functions.playerLeft(before, agentState, teams)

    #Vérifie si un joueur se fait attaquer et ou se fait emprisonner
    functions.playerAttack(agent, agentState)
    #Check states 
    for agentId in agentState.keys():

      #remet les joueurs en prison dans leurs prisons
      if agentState[agentId]['state'] == 1:
          functions.keepInJail(agentId, agent, agentState, jails)

      else:
          #libere les prisons lorsque un joueur libre de la meme equipe entre dans la prison
          if (agentState[agentId]['x'],agentState[agentId]['y']) in jails["Jail0"] and agentState[agentId]['team']== 0:
              functions.free(0, agent, agentState)
          elif (agentState[agentId]['x'],agentState[agentId]['y']) in jails["Jail1"] and agentState[agentId]['team'] == 1:
              functions.free(1, agent, agentState)
          elif (agentState[agentId]['x'],agentState[agentId]['y']) in jails["Jail2"] and agentState[agentId]['team'] == 2:
              functions.free(2, agent, agentState)

    #2eme partie du test permettant de tester en premier les fonctions d'attaque puis d'enprisonnement et d'attribution des points
    """
    agent.rulePlayer("joueur1","reqX", 47)
    agent.rulePlayer("joueur1","reqY", 47)
    agent.rulePlayer("joueur2","reqX", 46)
    agent.rulePlayer("joueur2","reqY", 46)
    agent.rulePlayer("joueur3","reqX", 45)
    agent.rulePlayer("joueur3","reqY", 45)
    """
    before = agentState
