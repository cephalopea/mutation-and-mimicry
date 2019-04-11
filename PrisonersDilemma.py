#Implementation of the Prisoners Dilemma
import random
import queue

#Main Loop, runs the game a specified number of times
def Main(gamesToPlay = 1000, playerOneStratagy = "random", playerTwoStratagy = "random"):
	playerOneScoreTotal = [] #Initialize the lists of points recieved. Could just add scores to an ongoing tally instead of summing lists, but thi sallows for future further analysis
	playerTwoScoreTotal = []

	for i in range(gamesToPlay): #Loop gamesToPlay number of times
		playerOneScore, playerTwoScore = PrisonersDilemma(Player(playerOneStratagy), Player(playerTwoStratagy)) #Run one game of the Prisoners Dilemma
		playerOneScoreTotal.append(playerOneScore) #Add results of games to the playerScore lists
		playerTwoScoreTotal.append(playerTwoScore)

	results = (sum(playerOneScoreTotal), sum(playerTwoScoreTotal))
	strategies = (playerOneStratagy, playerTwoStratagy)
	return(results, strategies)



#Translates user input into stratagies
def Player(stratagy):
	if stratagy == "defect": #Always returns Betray
		return("defect")
	elif stratagy == "cooperate": #Always returns Collaborate
		return("cooperate")
	elif stratagy == "random": #Randomly returns Collaborate or Betray
		return(RandomChoice())

#Randomly returns Collaborate or Betray
def RandomChoice():
	choices = ["cooperate", "defect"] #Create list of options
	return(random.choice(choices)) #Pick one and return it

#Play a game of the Prisoners Dilemma, assigning scores based on both players choices
def PrisonersDilemma(playerOneStratagy, playerTwoStratagy):
	if playerOneStratagy == "cooperate":
		if playerTwoStratagy == "cooperate":
			playerOneScore = 3
			playerTwoScore = 3
		elif playerTwoStratagy == "defect":
			playerOneScore = 0
			playerTwoScore = 5
	elif playerOneStratagy == "defect":
		if playerTwoStratagy == "cooperate":
			playerOneScore = 5
			playerTwoScore = 0
		elif playerTwoStratagy == "defect":
			playerOneScore = 1
			playerTwoScore = 1
	return(playerOneScore, playerTwoScore)

