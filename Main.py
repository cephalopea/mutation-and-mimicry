import PrisonersDilemma as PD
import evolution
import csv

def Main(cyclePrompt, mutationPrompt):
    cycles = int(input(cyclePrompt)) #number of times to cycle through games
    mutationPrompt = input(mutationPrompt)
    if mutationPrompt == "y":
        mutate = True
    else:
        mutate = False
    players = evolution.GenGen(9, 10) #Generate initial genomes (lists of game stratagies)
    for x in range(cycles): #run the simulation cycles number of times      
        for player in range(len(players)): #for each player
            others = [] #Declare list for other players
            for other in range(len(players)): #for each player
                if other > player: #if other players index is higher than current player
                    others.append(players[other]) #add them to list of other players for current player to play
            if others == []: #if we are on the last player, meaning everyone has already played everyone else
                break #break out and run Evolve
            for playerTwo in others: #for each player the current player will play
                players[player]['memory'] = [] #Wipe memory of games against previous players
                playerTwo['memory'] = []
                for z in range(9): #play ten games
                    strategy = players[player]['strategy'][z] #get the strategy for the current player
                    strategy2 = playerTwo['strategy'][z] #get the strategy for the current oponent
                    if strategy == 'steal':
                        if z > 0:
                            strategy = players[player]['memory'][-1] #player is the index, players is thelist of player dictionaries
                        else:
                            strategy = 'random'
                    if strategy2 == 'steal':
                        if z > 0:
                            strategy2 = playerTwo['memory'][-1]
                        else:
                            strategy2 = 'random'
                    result, strategies = PD.Main(1,strategy, strategy2) #play one game of prisoners dilemma
                    #print(playerTwo['memory'])
                    #print(strategies)
                    #print(strategies[0])
                    playerTwo['memory'].append(strategies[0]) #player two remembers the stratagy used by player one
                    players[player]['memory'].append(strategies[1]) #and vice versa
                    players[player]['gameResults'].append(result[0]) #Tell player one the result of game
        playerFitnessList = Fitness(players)
        playerGenomeList = Genomes(players)
        WriteToCSV(playerFitnessList, "FitnessData.csv")
        WriteToCSV(playerGenomeList, "GenomeData.csv")
        if mutate:
            evolution.MutateEvolve(players)
        else:
            evolution.Evolve(players)
    print("Run Completed")

def Fitness(players):
    playerFitnessList = []
    for player in players:
        playerFitness = evolution.Fitness(player)
        playerFitnessList.append(playerFitness)
    return(playerFitnessList)

def Genomes(players):
    playerGenomeList = []
    for player in players:
        playerGenome = player["strategy"]
        playerGenomeList.append(playerGenome)
    return(playerGenomeList)

def WriteToCSV(dataToWrite, name):
    with open(name, "a") as csvfile:
        dataWriter = csv.writer(csvfile)
        dataWriter.writerow(dataToWrite)

Main("Enter the number of generations to run the simulation for: ", "Enable mutation? (y/n): ")
