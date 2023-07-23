# Excersises and creating the four funtcions to make a tic tac toe gool gamee

display_board= ["_", "_", "_",
                "_", "_", "_",
                "_", "_", "_"]
currentPlayer= "X"
winner= None
gameRunning= True

#printing te game board
def printBoard(display_board):
    print(display_board[0] + " I " + display_board[1] + " I " + display_board[2])
    print("__________")
    print(display_board[3] + " I " + display_board[4] + " I " + display_board[5])
    print("__________")
    print(display_board[6] + " I " + display_board[7] + " I " + display_board[8])
    print("__________")
printBoard(display_board)
#take player input
def playerInput(display_board):
    inp = int(input("enter a number 1-9: "))
    if inp >= 1 and inp <= 9 and board[inp-1] == '-':
        board[inp-1] = currentplayer 
    else: 
        print("oops a player in already in the spot!")
    # player_input(player)

#check for win or tie 
def checkhorizontal(board):
    global winner
    if board(0) == board[1] == board[2] and board[1] !="-":
        winner = board[0]
        return True
    elif board[3] == board[4] == board[5] and board [3] != "-":
        winner = board[3]
        return True
    elif board[6] == board[7] == board[8] and board [6] != "-":
        winner = board[6]
        return True
    
def checkRow(board): 
    global winner 
    if board[0] == board[3] == board[6] and board[0] != "-":
        winner = board(0)
        return True
    elif board[1] == board[4] == board[7] and board[1] != "-":
        winner = board(0)
        return True
    elif board[2] == board[5] == board[8] and board[2] != "-":
        winner = board(2)
        return True
    
def checkdiag(board):
    global winner
    if board(0) == board(4) == board(8) and board(0) !="-":
       winner = board(0)
       return True
    elif board(2) == board(4) == board(6) and board(2) !="-":
       winner = board(2)
       return True
    

def checktie(board):
    if "-" not in  board:
        printBoard(display_board)
        print("its a tie!")
        gameRunning = False

def checkwin(): 
    if checkdiag or checkhorizontal or checkRow(display_board): 
        PRINT(F"THE WINNER IS {winner}")
 # check_win()

# switch the player
def switchplayer():
    global currentPlayer
    if currentPlayer == "X":
        currentPlayer = "0"
    else: 
        currentPlayer = "X"

#check for win or tie 
# play()

while gameRunning: 
    print(display_board)
    playerInput(display_board)
    checkwin()
    checktie()
    switchplayer()