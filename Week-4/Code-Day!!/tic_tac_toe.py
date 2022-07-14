from pickle import TRUE
from xmlrpc.client import boolean


board = [
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "]
]

def display_board() -> None:
    """a function to display the board in the screen"""

    content = 0
    row = 0
    print("\n")

    print ("TIC-TAC-TOE")
    for i in range(0, 7):
        
        if i == 0 or i == 6:
            print("*****************")
            
        elif i % 2 != 0:
            print(f"*   {board[row][content]} | {board[row][content + 1]} | {board[row] [content + 2]}   *")
            row += 1

        elif i % 2 == 0:
            print("* ----|---|---- *")

    print("\n")


def player_input(player: str) -> None :
    """a function to ge the input from the player and draw it on the board"""

    row = int(input("enter row: ")) - 1
    column = int(input("enter column: ")) - 1  
    
    if board[row][column] == " ":
        board[row][column] = player
    else:
        print("This spot is already taken you cheater !!! choose an other one")
        player_input(player)

    print("\n")


def check_win_row(row: int) -> bool:
    """fucntion to check if someone won by the horizontal"""

    next_case = 0
    if board[row][next_case] == board[row][next_case + 1] == board[row][next_case + 2] and board[row][next_case] != " ":
        return True


def check_win_col(col: int) -> bool:
    """fucntion to check if someone won by the vertical"""
    
    next_case = 0
    if board[next_case][col] == board[next_case + 1][col] == board[next_case + 2][col] and board[next_case][col] != " ":
        return True


def check_win_diag() -> bool:
    """fucntion to check if someone won by the diagonal"""
    
    diag = 0
    if board[diag][diag] == board[diag + 1][diag + 1] == board[diag + 2][diag + 2] and board[diag + 1][diag + 1] != " ":
        return True

    elif board[diag][diag + 2] == board[diag + 1][diag + 1] == board[diag + 2][diag] and board[diag + 1][diag + 1] != " ":
        return True


def check_win() -> bool:
    """fucntion that will check each turn if there is a winner """

    for row in range(0, 3):
        if check_win_row(row):
            return True 
        elif check_win_col(row):
            return True

    if(check_win_diag()):
        return True

    return False
    

display_board()
player_input("X")
print(check_win())
display_board()
player_input("X")
print(check_win())
display_board()
player_input("X")
print(check_win())
display_board()
