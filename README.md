# TennisGameScore
This is a simple program to track the scoring during a tennis game.

### Language: Python 3

## Assumptions
- Tie breakers are not considered
- Serve details are not tracked using the program.
- The game ends once a player wins two sets. The match would not continue until the completion of all 3 sets.

## Rules
- A game is won by the first player to have won at least four points in total and at least two points more than the opponent.
- The running score of each game is described in a manner peculiar to tennis: scores from zero to three points are described as "love", "fifteen", "thirty", and "forty" respectively.
- If at least three points have been scored by each player, and the scores are equal, the score is "deuce".
- If at least three points have been scored by each side and a player has one more point than his opponent, the score of the game is "advantage" for the player in the lead.
- A Set is won by the first player to have won at least 6 games in total and at least two games more than the opponent.
- A Match is won by player to win maximum of three sets (Best of three).

## Files Description
There are two Python files included in the repository 
- TennisScore.py
- testTennisScore.py

### TennisScore.py
  This is the implementation version of Tennis Game scoring. Start the game by providing the player's names. Begin a game by hitting ENTER. Once the game starts, input the winner of each point by pressing 1 for Player1 or 2 for Player2. For each point, the details are updated and the game winner is declared. Once a set is complete, the game moves on to the next set until there is a player having won 2 sets. The time taken to complete the match is displayed at the end of the program. 
    
### testTennisScore.py
  This is test version of Tennis Game scoring. The player names are hardcoded and the points are selected in random by the program. This is basically to get a random result from the program.

## Running the program
To run the program, open any of the files in command prompt by running the command

      python filename.py

Once the program starts, the first step would be to enter the names of player1 and player2. When **Press Enter to start the Game** prompt is displayed, hit on **ENTER**. Enter the winner of each point as per the hints mentioned in the program and proceed. Stats would be displayed at the end of each milestone. The program would end at the end of the match and the winner would be displayed.

Game stats would be displayed at the start of each game. Game stats include set number and the game number. Match stats include winner of the set, game and match. Match scores would be displayed at the end of each game, set and match. Number of games won by each player in every set is displayed here. 
