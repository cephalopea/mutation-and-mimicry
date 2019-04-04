import PrisonersDilemma as PD
import evolution

def Main(cyclePrompt):
    cycles = int(input(cyclePrompt))
    
    for x in range(cycles): #run the simulation cycles number of times
        players = evolution.GenGen()
        for player in players:

            for y in range(7):
                for z in range(9):
                    strategy = player[strategy][z]
                    strategy2 = players
                    result = PD.Main(1,strategy, strategy2)




Main("Enter the number of cycles to run the simulation for: ")