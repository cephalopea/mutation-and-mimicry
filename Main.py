import PrisonersDilemma as PD
import evolution

def Main(cyclePrompt):
    cycles = int(input(cyclePrompt)) #number of times to cycle through games
    players = evolution.GenGen() #Generate initial genomes (lists of game stratagies)
    for x in range(cycles): #run the simulation cycles number of times      
        for player in range(players): #for each player
            others = [] #Declare list for other players
            for other in range(players): #for each player
                if other > player: #if other players index is higher than current player
                    others.append(players[other]) #add them to list of other players for current player to play
            if others == []: #if we are on the last player, meaning everyone has already played everyone else
                break #break out and run Evolve
            for playerTwo in others: #for each player the current player will play
                players[player][memory] = [] #Wipe memory of games against previous players
                playerTwo[memory] = []
                for z in range(9): #play ten games
                    strategy = players[player][strategy][z] #get the stratagy for the current player
                    strategy2 = playerTwo[strategy][z] #get the stratagy for the current oponent
                    result, stratagies = PD.Main(1,strategy, strategy2) #play one game of prisoners dilemma
                    playerTwo[memory][z] = stratagies[0] #player two remembers the stratagy used by player one
                    players[player][memory][z] = stratagies[1] #and vice versa
                    players[player][gameResults].append(result[0]) #Tell player one the result of game
        evolution.Evolve(players)



Main("Enter the number of cycles to run the simulation for: ")