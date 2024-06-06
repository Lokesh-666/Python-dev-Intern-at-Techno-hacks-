import random
import time

# Initialize the game board
theBoard = {'1': ' ', '2': ' ', '3': ' ',
            '4': ' ', '5': ' ', '6': ' ',
            '7': ' ', '8': ' ', '9': ' '}

# Function to print the current state of the board
def printBoard(theBoard):
    print(theBoard['1'] + '|' + theBoard['2'] + '|' + theBoard['3'])
    print('-+-+-')
    print(theBoard['4'] + '|' + theBoard['5'] + '|' + theBoard['6'])
    print('-+-+-')
    print(theBoard['7'] + '|' + theBoard['8'] + '|' + theBoard['9'])

# Function to check if there is a winner
def checkForWin(theBoard):
    if theBoard['1'] == theBoard['2'] == theBoard['3'] != ' ':
        return theBoard['1']
    elif theBoard['4'] == theBoard['5'] == theBoard['6'] != ' ':
        return theBoard['4']
    elif theBoard['7'] == theBoard['8'] == theBoard['9'] != ' ':
        return theBoard['7']
    elif theBoard['1'] == theBoard['4'] == theBoard['7'] != ' ':
        return theBoard['1']
    elif theBoard['2'] == theBoard['5'] == theBoard['8'] != ' ':
        return theBoard['2']
    elif theBoard['3'] == theBoard['6'] == theBoard['9'] != ' ':
        return theBoard['3']
    elif theBoard['1'] == theBoard['5'] == theBoard['9'] != ' ':
        return theBoard['1']
    elif theBoard['3'] == theBoard['5'] == theBoard['7'] != ' ':
        return theBoard['3']
    else:
        return None

# Function for the PC to make a move
def pcPlays(theBoard):
    available_moves = [k for k, v in theBoard.items() if v == ' ']
    pcPlayed = random.choice(available_moves)
    theBoard[pcPlayed] = 'O'

# Function to announce the winner for Player vs PC game
def announceWinnerPlayerVsPC(WhoWon):
    if WhoWon == 'X':
        print("You won!")
    elif WhoWon == 'O':
        print("The PC won!")
    elif WhoWon == None:
        print("It's a tie!")

# Function to announce the winner for Player vs Player game
def announceWinnerPlayerVsPlayerTicTacToe(WhoWon):
    if WhoWon == 'X':
        print("Player 1 Won!")
    elif WhoWon == 'O':
        print("Player 2 Won!")
    elif WhoWon == None:
        print("It's a tie!")

# Function for Player vs PC game
def PlayerVsPc_tic_tac_toe():
    printBoard(theBoard)
    print("Let me play first... ")
    pcPlays(theBoard)
    time.sleep(5)
    printBoard(theBoard)
    WhoWon = None
    i = 0
    while (WhoWon == None):
        if (i >= 4):
            break
        print("Where do you wish to play? (1 to 9)")
        player = int(input())
        if theBoard[str(player)] == ' ':
            theBoard[str(player)] = 'X'
            printBoard(theBoard)
        else:
            print("That spot is already taken. Try again.")
            continue
        WhoWon = checkForWin(theBoard)

        if WhoWon == None:
            print("It's the PC's turn now...")
            time.sleep(5)
            pcPlays(theBoard)
            printBoard(theBoard)
            WhoWon = checkForWin(theBoard)
        i = i + 1
    announceWinnerPlayerVsPC(WhoWon)

# Function for Player vs Player game
def playerVsPlayerTicTacToe():
    printBoard(theBoard)
    WhoWon = None
    i = 0
    while (i <= 4 and WhoWon == None):
        print("Where does Player 1 (X) want to play? ")
        player1 = int(input())
        if theBoard[str(player1)] == ' ':
            theBoard[str(player1)] = 'X'
            printBoard(theBoard)
        else:
            print("That spot is already taken. Try again.")
            continue
        WhoWon = checkForWin(theBoard)

        if WhoWon == None and i <= 3:
            while (1):
                print("Where does Player 2 (O) want to play? ")
                player2 = int(input())
                if theBoard[str(player2)] == ' ':
                    theBoard[str(player2)] = 'O'
                    printBoard(theBoard)
                    break
                else:
                    print("That spot is already taken. Try again.")
                    continue
            WhoWon = checkForWin(theBoard)
        i+=1
    announceWinnerPlayerVsPlayerTicTacToe(WhoWon)

# Main function to start the game
def main():
    print("Do you wish to play tic tac toe with PC? (y/n): ")
    answer = input()
    if answer.lower() == "y":
        PlayerVsPc_tic_tac_toe()
    else:
        print("Okay, do you wish to play against another player? (y/n): ")
        answer = input()
        if answer.lower() == "y":
            playerVsPlayerTicTacToe()

if __name__ == '__main__':
    main()
