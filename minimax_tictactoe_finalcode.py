import copy, sys, time, random

# given a game state
# generate all possible moves up until the terminal states
# evaluate each terminal state's heuristic value
# find out the optimum path to take to maximize win and/or minimize loss
# computermove function should return a board space


tictactoeBoard = {'1': ' ', '2': ' ', '3' :' ',
                  '4': ' ', '5': ' ', '6' :' ',
                  '7': ' ', '8': ' ', '9' :' '}

def printBoard(board):
    print ('| ' + board['1'] + ' || ' + board['2'] + ' || ' + board['3'] + ' |')
    print ('---------------')
    print ('| ' + board['4'] + ' || ' + board['5'] + ' || ' + board['6'] + ' |')
    print ('---------------')
    print ('| ' + board['7'] + ' || ' + board['8'] + ' || ' + board['9'] + ' |')

def instruc():
    welcomemsg = ('  Welcome! Try to beat the tic-tac-toe machine if you can!  ')
    print(welcomemsg.center(60, '#'))
    print('')
    print('IMPORTANT INSTRUCTION:')
    print('Take note of the following moves you should type when the game prompts you to input a space.')
    print('')
    print('| 1 || 2 || 3 |')
    print('---------------')
    print('| 4 || 5 || 6 |')
    print('---------------')
    print('| 7 || 8 || 9 |')
    print('')
    print('')

def spaceIsValid(board, s):
    if s in board.keys():
        return True

def spaceIsFree(board, s):
    if board[s] == ' ':
        return True
    
def winningCombo(board, m, L, M, R):
    if board[L] == m and board[M] == m and board[R] == m:
        return True

def check4WinningCombo(board, m):
    if winningCombo(board, m, '1', '2', '3'):
        return True
    if winningCombo(board, m, '4', '5', '6'):
        return True
    if winningCombo(board, m, '7', '8', '9'):
        return True
    if winningCombo(board, m, '1', '5', '9'):
        return True
    if winningCombo(board, m, '3', '5', '7'):
        return True
    if winningCombo(board, m, '1', '4', '7'):
        return True
    if winningCombo(board, m, '2', '5', '8'):
        return True
    if winningCombo(board, m, '3', '6', '9'):
        return True

def turnsMaxedOut(board):
    for noValueKeys in board.keys():
        if spaceIsFree(board, noValueKeys):
            return False
    return True
        
def computers_turn(state, move):
    if move == 'X':
        bestspace = getmax(state, move)[1]
    elif move == 'O':
        bestspace = getmin(state, move)[1]
    return bestspace
        
def getmax(state, move):
    bestvalue = -100
    bestspace = 0
    for space in state.keys():
        if spaceIsFree(state, space):
##            print(state)
            state_simulation = copy.deepcopy(state)
            state_simulation[space] = move
##            print(state_simulation)
            if check4WinningCombo(state_simulation, move):
                terminal = 1
##                print(str(terminal) + ' : terminal')
            elif turnsMaxedOut(state_simulation):
                terminal = 0
##                print(str(terminal) + ' : terminal')
            else:
                nodevalues = getmin(state_simulation, 'O')
                terminal = nodevalues[0]
##                print(str(terminal) + ' : terminal')

            if terminal > bestvalue:
                bestvalue = terminal
                bestspace = space
    return (bestvalue, bestspace)
        
def getmin(state, move):
    bestvalue = 100
    bestspace = 0
    for space in state.keys():
        if spaceIsFree(state, space):
##            print(state)
            state_simulation = copy.deepcopy(state)
            state_simulation[space] = move
##            print(state_simulation)
            if check4WinningCombo(state_simulation, move):
                terminal = -1
##                print(str(terminal) + ' : terminal')
            elif turnsMaxedOut(state_simulation):
                terminal = 0
##                print(str(terminal) + ' : terminal')
            else:
                nodevalues = getmax(state_simulation, 'X')
                terminal = nodevalues[0]
##                print(str(terminal) + ' : terminal')

            if terminal < bestvalue:
                bestvalue = terminal
                bestspace = space
    return (bestvalue, bestspace)

def trash_talk():
    saytheff = ["\"Implying you'll win.\"", "\"It's happeniiiing!!!\"", "\"HABEENIIIIIN\"", "\"AI master race\"", "\"Gotta make my master proud.\"", "\"Why do you even play this game?\"", "\"Not gonna happen, dude.\"", "\"I'm actually starting to get bored.\"", "\"Imma try to prolong this game to give you a chance.\""]
    num = [0,1,2,3,4,5,6,7,8]
    return saytheff[random.choice(num)]
                    
def playTheGame():
    
    instruc()
    for k in tictactoeBoard.keys():
        tictactoeBoard[k] = ' '
        
    printBoard(tictactoeBoard)

    print ('Human, pick X or O, or none to end game.')
    print ('(X goes first)')

    move = input()
    move = move.upper()

    while True:
        if move == 'X':
            print ('You go first.')
            for turns in range (5):
                move = 'X'
                print ('Pick a space.')
                space = input()
                while True:
                    if spaceIsValid(tictactoeBoard, space) and spaceIsFree(tictactoeBoard, space):
                        tictactoeBoard[space] = move
                        printBoard(tictactoeBoard)
                        break
                    else:
                        print('Either the space you entered is not valid or it is already taken. See instructions above and pick again.')
                        space = input()
                        continue
                if check4WinningCombo(tictactoeBoard, move):
                    print('Human wins the game. Game ends here.')
                    print('Do you want to play again? Y/N')
                    playAgain = input()
                    playAgain = playAgain.upper()
                    while True:
                        if playAgain == 'Y':
                            playTheGame()
                        elif playAgain == 'N':
                            print('Exiting game...')
                            time.sleep(5)
                            sys.exit()
                        else:
                            print('Type only either Y for yes and N for no.')
                            playAgain = input()
                            playAgain = playAgain.upper()
                elif turnsMaxedOut(tictactoeBoard):
                    print ('Nobody won the game. Game ends here.')
                    print('Do you want to play again? Y/N')
                    playAgain = input()
                    playAgain = playAgain.upper()
                    while True:
                        if playAgain == 'Y':
                            playTheGame()
                        elif playAgain == 'N':
                            print('Exiting game...')
                            time.sleep(5)
                            sys.exit()
                        else:
                            print('Type only either Y for yes and N for no.')
                            playAgain = input()
                            playAgain = playAgain.upper()
                else:
                    move = 'O'
                    print ('Please wait while the computer makes its move.')
                    space = computers_turn(tictactoeBoard, move)
                    tictactoeBoard[space] = move
                    printBoard(tictactoeBoard)
                    print(trash_talk())
                    if check4WinningCombo(tictactoeBoard, move):
                        print('The computer wins the game. Game ends here.')
                        print('Do you want to play again? Y/N')
                        playAgain = input()
                        playAgain = playAgain.upper()
                        while True:
                            if playAgain == 'Y':
                                playTheGame()
                            if playAgain == 'N':
                                print('Exiting game...')
                                time.sleep(5)
                                sys.exit()
                            else:
                                print('Type only either Y for yes and N for no.')
                                playAgain = input()
                                playAgain = playAgain.upper()
            
        if move == 'O':
            print('The computer will go first.')
            for turns in range (5):
                move = 'X'
                print ('Please wait while the computer makes its move.')
                if turns == 0:
                    firstmove = ['1','2','3','4','5','6','7','8','9']
                    space = random.choice(firstmove)
                elif turns > 0:
                    space = computers_turn(tictactoeBoard, move)
                
                tictactoeBoard[space] = move
                printBoard(tictactoeBoard)
                print(trash_talk())
                if check4WinningCombo(tictactoeBoard, move):
                    print('The computer wins the game. Game ends here.')
                    print('Do you want to play again? Y/N')
                    playAgain = input()
                    playAgain = playAgain.upper()
                    while True:
                        if playAgain == 'Y':
                            playTheGame()
                        elif playAgain == 'N':
                            print('Exiting game...')
                            time.sleep(5)
                            sys.exit()
                        else:
                            print('Type only either Y for yes and N for no.')
                            playAgain = input()
                            playAgain = playAgain.upper()
                elif turnsMaxedOut(tictactoeBoard):
                    print ('Nobody won the game. Game ends here.')
                    print('Do you want to play again? Y/N')
                    playAgain = input()
                    playAgain = playAgain.upper()
                    while True:
                        if playAgain == 'Y':
                            playTheGame()
                        elif playAgain == 'N':
                            print('Exiting game...')
                            time.sleep(5)
                            sys.exit()
                        else:
                            print('Type only either Y for yes and N for no.')
                            playAgain = input()
                            playAgain = playAgain.upper()
                else:
                    print('It is now your turn. Pick a space.')
                    move = 'O'
                    space = input()
                    while True:
                        if spaceIsValid(tictactoeBoard, space) and spaceIsFree(tictactoeBoard, space):
                            tictactoeBoard[space] = move
                            printBoard(tictactoeBoard)
                            break
                        else:
                            print('Either the space you entered is not valid or it is already taken. See instructions above and pick again.')
                            space = input()
                            continue
                    if check4WinningCombo(tictactoeBoard, move):
                        print('Human wins the game. Game ends here.')
                        print('Do you want to play again? Y/N')
                        playAgain = input()
                        playAgain = playAgain.upper()
                        while True:
                            if playAgain == 'Y':
                                playTheGame()
                            elif playAgain == 'N':
                                print('Exiting game...')
                                time.sleep(5)
                                sys.exit()
                            else:
                                print('Type only either Y for yes and N for no.')
                                playAgain = input()
                                playAgain = playAgain.upper()           

        if move == '':
            print ('You chose to quit the game.')
            time.sleep(3)
            sys.exit()

        else:
            print ('Pick only either X or O.')
            move = input()
            move = move.upper()
            continue

playTheGame()

##test_board = {'1': 'X', '2': 'X', '3' :'O',
##              '4': ' ', '5': 'O', '6' :' ',
##              '7': 'X', '8': ' ', '9' :'O'}

##move = 'X'

##print(computers_turn(test_board, move))

