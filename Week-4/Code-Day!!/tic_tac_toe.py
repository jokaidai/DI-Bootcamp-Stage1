def display_board() -> None:
    """a function to display the board in the screen"""

board = [
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "]
]

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

   
        

display_board()