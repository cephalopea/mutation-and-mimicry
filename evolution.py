#creates a random starting strategy with between 1 and 5 elements
#returns a list of strings (should be either "defect" or "cooperate")
def randomStrategy():
    strategies = ["defect", "cooperate"]
    playerStrat = []
    stratLength = random.randint(4)
    for (i = 0; i < stratLength, i++):
        playerStrat.append(strategies[random.randint(1)])
    return playerStrat

#accepts a list of integers (should be the util results of the player's most recent round of games)
#returns a single integer that indicates a player's fitness (super simple for now, can improve later)
def fitness(gameResults):
    return sum(gameResults)


    
#use a switch case and a random integer to select a random function