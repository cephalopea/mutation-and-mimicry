import PrisonersDilemma



def Main(cyclePrompt):
    cycles = int(input(cyclePrompt))
        
    for i in range(cycles):
        #run the simulation cycles number of times
        print(i)



def StrategyTracker(change,p1,p2,p3,p4,p5,p6,p7,p8,p9):
    if change:
        Player1Strat = p1
        Player2Strat = p2
        Player3Strat = p3
        Player4Strat = p4
        Player5Strat = p5
        Player6Strat = p6
        Player7Strat = p7
        Player8Strat = p8
        Player9Strat = p9
    else
    return(p1,p2,p3,p4,p5,p6,p7,p8,p9)

Main("Enter the number of cycles to run the simulation for: ")