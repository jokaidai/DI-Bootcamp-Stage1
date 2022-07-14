import random

# global variable
board = [
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "]
]

player = " "
# global variable

def display_board() -> None:
    """a function to display the board in the screen"""

    content = 0
    row = 0

    print ("TIC-TAC-TOE")
    for i in range(0, 7):
        
        if i == 0 or i == 6:
            print("*****************")
            
        elif i % 2 != 0:
            print(f"*   {board[row][content]} | {board[row][content + 1]} | {board[row] [content + 2]}   *")
            row += 1

        elif i % 2 == 0:
            print("* ----|---|---- *")


def choose_player() -> str: 
    """function to choose who's gonna start the X or the O and then change the player each turn accordingly"""

    if player == " ": # only during first call
        
        print("To choose who is starting let's flip a coin ...\n")
        coin = random.randint(1, 2) 

        if coin == 1:
            print("Player X is starting, good luck !!!\n")
            return "X"
        else:
            print("Player O is starting, good luck !!!\n")
            return "O"

    elif player == "X":
        return "O"
    
    elif player == "O":
        return "X"


def player_input(player: str) -> None : 
    """a function to ge the input from the player and draw it on the board"""

    global board
    row = int(input("enter row: ")) - 1
    column = int(input("enter column: ")) - 1  
    
    if board[row][column] == " ":
        board[row][column] = player
    else:
        print("This spot is already taken you cheater !!! choose an other one")
        player_input(player)

    print("\n")


def check_win_row(row: int) -> bool: #-------------this function is called only in the check_win function
    """fucntion to check if someone won by the horizontal"""

    next_case = 0
    if board[row][next_case] == board[row][next_case + 1] == board[row][next_case + 2] and board[row][next_case] != " ":
        return True


def check_win_col(col: int) -> bool: #-------------this function is called only in the check_win function
    """fucntion to check if someone won by the vertical"""
    
    next_case = 0
    if board[next_case][col] == board[next_case + 1][col] == board[next_case + 2][col] and board[next_case][col] != " ":
        return True


def check_win_diag() -> bool: #-------------this function is called only in the check_win function
    """fucntion to check if someone won by the diagonal"""
    
    diag = 0
    if board[diag][diag] == board[diag + 1][diag + 1] == board[diag + 2][diag + 2] and board[diag + 1][diag + 1] != " ":
        return True

    elif board[diag][diag + 2] == board[diag + 1][diag + 1] == board[diag + 2][diag] and board[diag + 1][diag + 1] != " ":
        return True


def check_tie() -> bool:
    """function to check if the game is tie (nobody won)"""

    for row in range(0, 3):
        for col in range(0, 3):
            if " " in board[row][col]:
                return False
    return True


def check_win() -> bool:
    """fucntion that will check each turn if there is a winner by calling other function for each type of win"""

    for row in range(0, 3):
        if check_win_row(row):
            return True 
        elif check_win_col(row):
            return True

    if(check_win_diag()):
        return True

    return False


def game_over() -> None:
    """function to send messages if the game is over acoordingly to the result"""

    if check_win():
        
        print(f"Player: {player} won !!! ")
    else:
        print("Its a tie !!! better luck next time !!!")


def play() -> None:
    """main function that handle the entire game session"""

    global player # we want to change the value of the global player variable not the local so it remenber wich player is actually playing 

    print("\nWelcome to TIC-TAC-TOE !!!\n")
    display_board()
    player = choose_player()
 
    while True:
        
        player_input(player)
        display_board()
        if check_tie() or check_win():
            break
        player = choose_player()
        print(f"Player: {player}  turn ...\n")   
       
    game_over()

play()
