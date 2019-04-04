#Implementation of the Prisoners Dilemma
import random
import queue

#Main Loop, runs the game a specified number of times
def Main(gamesToPlay = 1000, playerOneStratagy = 'Random', playerTwoStratagy = 'Random'):
	playerOneScoreTotal = [] #Initialize the lists of points recieved. Could just add scores to an ongoing tally instead of summing lists, but thi sallows for future further analysis
	playerTwoScoreTotal = []

	for i in range(gamesToPlay): #Loop gamesToPlay number of times
		playerOneScore, playerTwoScore = PrisonersDilemma(Player(playerOneStratagy), Player(playerTwoStratagy)) #Run one game of the Prisoners Dilemma
		playerOneScoreTotal.append(playerOneScore) #Add results of games to the playerScore lists
		playerTwoScoreTotal.append(playerTwoScore)

	results = (sum(playerOneScoreTotal), sum(playerTwoScoreTotal))
	return(results)



#Translates user input into stratagies
def Player(stratagy):
	if stratagy == 'Betray': #Always returns Betray
		return('Betray')
	elif stratagy == 'Collaborate': #Always returns Collaborate
		return('Collaborate')
	elif stratagy == 'Random': #Randomly returns Collaborate or Betray
		return(RandomChoice())

#Randomly returns Collaborate or Betray
def RandomChoice():
	choices = ['Collaborate', 'Betray'] #Create list of options
	return(random.choice(choices)) #Pick one and return it

#Play a game of the Prisoners Dilemma, assigning scores based on both players choices
def PrisonersDilemma(playerOneStratagy, playerTwoStratagy):
	if playerOneStratagy == 'Collaborate':
		if playerTwoStratagy == 'Collaborate':
			playerOneScore = 3
			playerTwoScore = 3
		elif playerTwoStratagy == 'Betray':
			playerOneScore = 0
			playerTwoScore = 5
	elif playerOneStratagy == 'Betray':
		if playerTwoStratagy == 'Collaborate':
			playerOneScore = 5
			playerTwoScore = 0
		elif playerTwoStratagy == 'Betray':
			playerOneScore = 1
			playerTwoScore = 1
	return(playerOneScore, playerTwoScore)

