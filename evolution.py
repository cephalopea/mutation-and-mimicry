strategies = ["defect", "cooperate"]
samplePlayer = {"strategy": ["defect", "cooperate", "defect", "cooperate", "defect", "cooperate", "defect", "cooperate", "defect", "cooperate"], "memory": [], "gameResults": []}

#returns a random integer between 0 and the index of the last element of the collection (n-1), inclusive
def BoundedRand(collection):
    return random.randint(0, (len(collection) - 1))

#creates a random starting strategy with 10 elements
#returns a list of strings (should be either "defect" or "cooperate")
def RandomStrategy(length):
    playerStrat = []
    stratLength = random.randint(0, length)
    for (i = 0; i < stratLength, i++):
        playerStrat.append(strategies[boundedRand(strategies)])
    return playerStrat

#accepts a list of integers (should be the util results of the player's most recent round of games)
#returns a single integer that indicates a player's fitness (super simple for now, can improve later)
def Fitness(gameResults):
    return sum(gameResults)

#picks a random point in the genome and replaces it with a random strategy from strategies
#returns a genome with same length as input genome
def Mutate(genome):
    mutationPoint = boundedRand(genome)
    genome[mutationPoint] = strategies[boundedRand(strategies)]
    return genome

#crosses over two genomes of the same length
#returns a new genome with the beginning of genome1 and the end of genome2, same length as input genomes
def Crossover(genome1, genome2):
    crossOverPoint = random.randint(0, len(genome2))
    section1 = genome1[0:(crossOverPoint - 1)]
    section2 = genome[crossOverPoint:len(genome2)]
    return section1 + section2

#select the best subset of the given population
#returns a collection of players and their fitness scores
def Select(population, number):
    selectedPlayers = []
    for player in population:
        fit = Fitness(player["gameResults"])
        if (len(selectedPlayers) < number):
            selectedPlayers.append({"player": player, "fitness": fit})
        else:
            for opponent in selectedPlayers:
                if (fit > opponent["fitness"]):
                    selectedPlayers.remove(opponent)
                    selectedPlayers.append({"player": player, "fitness": fit})
                    break
    
def Evolve():
#use a switch case and a random integer to select a random function

def GenGen():
    