import j2l.pytactx.agent as pytactx
import functions

"""Création of the arena"""
functions.createRules(agent)



before = []
teams = [0,0,0]
# Affichage dans l'arène du début de la partie par l'agent
agent.ruleArena("info", "🟢 C'est parti !")

agent.update()

agents = {
    "Poule": {
        "x": 0,
        "y": 0,
    },
    "Renard": {
        "x": 5,
        "y": 7,
    },
    "Viper": {
        "x": 13,
        "y": 3,
    }
}
for agentId, attributes in agents.items():
    for attributeKey, attributeValue in attributes.items():
        agent.rulePlayer(agentId, attributeKey, attributeValue)

#agentState{agentId: {"state": 0||1, "x":x, "y":y, "team":team}}
agentState = {}


#map

jails = functions.getJailPosition(agent)
while True:

    agent.update()

    for agentId in agent.range.keys():
      #Add new agents in dict
        if agentId not in agentState.keys():
            functions.playerAppeared(agentState, agentId, agent, teams)

      #Update agents's position
        agentState[agentId]['x'] = agent.range[agentId]["x"]
        agentState[agentId]['y'] = agent.range[agentId]["y"]
        agentState[agentId]['x'] = agent.range[agentId]['x']
        agentState[agentId]['y'] = agent.range[agentId]['y']
        agentState[agentId]['life'] = agent.range[agentId]['life']
        agentState[agentId]['score'] = agent.range[agentId]['score']

    """Management of new players in the arena"""

    functions.playerLeft(before, agentState, teams)

    functions.playerAttack(agent, agentState)
    #Check states 
    for agentId in agentState.keys():

      #Keep agent in their prisons
      if agentState[agentId]['state'] == 1:
          functions.keepInJail(agentId, agent, agentState, jails)

      else:
          #Check if agents are free
          if (agentState[agentId]['x'],agentState[agentId]['y']) in jails["Jail0"] and agentState[agentId]['team']== 0:
              functions.free(0, agent, agentState)
          elif (agentState[agentId]['x'],agentState[agentId]['y']) in jails["Jail1"] and agentState[agentId]['team'] == 1:
              functions.free(1, agent, agentState)
          elif (agentState[agentId]['x'],agentState[agentId]['y']) in jails["Jail2"] and agentState[agentId]['team'] == 2:
              functions.free(2, agent, agentState)

    agent.rulePlayer("Renard","x", 47)
    agent.rulePlayer("Renard","y", 47)
    agent.rulePlayer("Poule","x", 46)
    agent.rulePlayer("Poule","y", 46)

    before = agentState
