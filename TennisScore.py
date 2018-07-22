import time
from datetime import timedelta

# Display Match Score
def matchScoreDisplay():
	spaceFiller = max(len(players[0]), len(players[1]), len('SET')) + 4  # To obtain equal spacing of names when scores are displayed
	print('-------------------------')
	print('MATCH SCORE')
	print('-------------------------')
	print('SET' + ' ' * (spaceFiller - 3) + ' '.join(str(i) for i in range(1, len(matchScore) + 1)))
	print('-------------------------')
	print(players[0] + ' ' * (spaceFiller - len(players[0])) + ' '.join(str(matchScore[j][0]) for j in range(len(matchScore))))
	print(players[1] + ' ' * (spaceFiller - len(players[1])) + ' '.join(str(matchScore[j][1]) for j in range(len(matchScore))))
	print('-------------------------')

# Display Current Game Score
def gameScoreDisplay(score):
	scoreDict = {0: '0', 1: '15', 2: '30', 3: '40'}
	# Deuce
	if max(score) > 2 and score[0] == score[1]: 
		print('Deuce !')
	# Advantage
	elif max(score) > 3 and score[0] != score[1]:
		print('Advantage ' + players[score.index(max(score))])
	else:
		print('Game Score: ' + scoreDict[score[0]] + ' - ' + scoreDict[score[1]])

# Complete a game		
def playGame():
	scoreDict = {0: '0', 1: '15', 2: '30', 3: '40'}
	playerScore = [0, 0]
	vaildEntry = True

	while(1):
		while(1):
			try:
				pointWinner = int(input('Point Winner? 1 for '+ players[0] + ' 2 for ' + players[1] + ': '))
				if pointWinner in [1, 2]:
					break
				print('Please enter a valid response.')
			except:
				print('Please enter a valid response.')

		playerScore[pointWinner-1] += 1

		if abs(playerScore[0] - playerScore[1]) > 1 and max(playerScore) > 3:
			gameWinner = playerScore.index(max(playerScore))
			return gameWinner

		gameScoreDisplay(playerScore)

players = []
print('Tennis Game Scoring')
players.append(str(input('Enter the name of player1: '))) 
players.append(str(input('Enter the name of player2: ')))  

print ('__________'+ players[0] + ' vs ' + players[1] + '__________')
startTime = time.time()
gameNumber = 1
setNumber = 1
setsWon = [0, 0]
setScore = [0, 0]
matchScore = [[0, 0]]

while(1):
	# Print Game Stats
	input('Press Enter to start the Game')
	print('--------------------------------')
	print('GAME STATS')
	print('--------------------------------')
	print('Game Number - '+ str(gameNumber))
	print('Set Number - '+ str(setNumber))
	print('--------------------------------')

	# Complete a game
	winnerGame = playGame()

	print('--------------------------------')
	print('Game Ended. Winner - ' + players[winnerGame])
	setScore[winnerGame] += 1
	matchScore[setNumber-1]  = list(setScore)
	matchScoreDisplay()
	gameNumber += 1

	# Check for completion of set
	if abs(setScore[0] - setScore[1]) > 1 and max(setScore) > 5:
		print('Set Completed')
		print('Set Winner - ' + players[setScore.index(max(setScore))])
		setNumber += 1
		setsWon[setScore.index(max(setScore))] += 1
		setScore = [0, 0]
		matchScore.append([0, 0])

		# Check for completion of Match
		if max(setsWon) == 2:
			print('Match Completed')
			print('Winner of the Match - ' + players[setScore.index(max(setScore))])	
			matchScore.pop()
			matchScoreDisplay()
			print('Match completed in %s' % (timedelta(seconds = round(time.time() - startTime))))
			break
	
