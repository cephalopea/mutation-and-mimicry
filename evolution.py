import numpy

strategies = ["defect", "cooperate", "steal"]
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
        playerStrat.append(strategies[BoundedRand(strategies)])
    return playerStrat

#accepts a list of integers (should be the util results of the player's most recent round of games)
#returns a single integer that indicates a player's fitness (super simple for now, can improve later)
def Fitness(gameResults):
    return sum(gameResults)

#picks a random point in the genome and replaces it with a random strategy from strategies
#returns a genome with same length as input genome
def Mutate(genome):
    mutationPoint = BoundedRand(genome)
    genome[mutationPoint] = strategies[BoundedRand(strategies)]
    return genome

#crosses over two genomes of the same length
#returns a new genome with the beginning of genome1 and the end of genome2, same length as input genomes
def Crossover(genome1, genome2):
    crossOverPoint = BoundedRand(genome2)
    section1 = genome1[0:(crossOverPoint - 1)]
    section2 = genome[crossOverPoint:len(genome2)]
    return section1 + section2

#selects the best individuals out of subsets of the total population, given a percentage of pop to select
#returns an array of successful individual players
def Select(population, selectNum):
    numpy.random.shuffle(population)
    selected = []
    #next line from https://stackoverflow.com/questions/2130016/splitting-a-list-into-n-parts-of-approximately-equal-length/37414115
    subsets = [population[i::selectNum] for i in xrange(selectNum)]
    for subset in subsets:
        selectedPlayer = None
        for player in subset:
            fit = Fitness(player["gameResults"])
            if (!selectedPlayer):
                selectedPlayer = {}
                selectedPlayer["player"] = player
                selectedPlayer["fitness"] = fit
            else:
                if (fit > selectedPlayer["fitness"]):
                    selectedPlayer = {}
                    selectedPlayer["player"] = player
                    selectedPlayer["fitness"] = fit
        selected.append(selectedPlayer["player"])
    return selected

#returns an evolved population using crossover 
def Evolve(population):
#use a switch case and a random integer to select a random function
    breedPop = Select(population, len(population)/2)
    remainPop = Select(population, len(population)/2)
    nextGen = []
    for (i = 0; i < len(breedPop); i++):
        newPlayer = {}
        newPlayer["gameResults"] = []
        newPlayer["memory"] = []
        randOne = breedPop[BoundedRand(breedPop)]
        randTwo = breedPop[BoundedRand(breedPop)]
        newPlayer["strategy"] = Crossover(randOne["strategy"], randTwo["strategy"])
        nextGen.append(newPlayer)
    nextGen = nextGen + remainPop
    numpy.random.shuffle(nextGen)
    return nextGen

#returns an evolved population using mutation and crossover
def MutateEvolve(population):
#use a switch case and a random integer to select a random function
    breedPop = Select(population, len(population)/3)
    mutatePop = Select(population, len(population)/3)
    remainPop = Select(population, len(population)/3)
    nextGen = []
    for (i = 0; i < len(breedPop); i++):
        newPlayer = {}
        newPlayer["gameResults"] = []
        newPlayer["memory"] = []
        randOne = breedPop[BoundedRand(breedPop)]
        randTwo = breedPop[BoundedRand(breedPop)]
        newPlayer["strategy"] = Crossover(randOne["strategy"], randTwo["strategy"])
        nextGen.append(newPlayer)
    for (i = 0; i < len(mutatePop); i++):
        newPlayer = {}
        newPlayer["gameResults"] = []
        newPlayer["memory"] = []
        newPlayer["strategy"] = Mutate(mutatePop[i]["strategy"])
        nextGen.append(newPlayer)
    nextGen = nextGen + remainPop
    numpy.random.shuffle(nextGen)
    return nextGen

#generates an initial generation of players
#returns an array of players
def GenGen(popsize, stratlength):
    generation = []
    for (i = 0; i < popsize; i++):
        newPlayer = {}
        newPlayer["strategy"] = RandomStrategy(stratlength)
        newPlayer["memory"] = []
        newPlayer["gameResults"] = []
        generation.append(newPlayer)
    return generation
    