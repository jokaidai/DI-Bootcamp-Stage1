import re
from typing import final
# Instructions
# Hint: Look at the remote learning “Matrix” videos

# The matrix is a grid of strings (alphanumeric characters and spaces) with a hidden message in it.
# To decrypt the matrix, Neo reads each column from top to bottom, starting from the leftmost column, select only the alpha characters and connect them, then he replaces every group of symbols between two alpha characters by a space.

# Using his technique, try to decode this matrix:

#     7i3
#     Tsi
#     h%x
#     i #
#     sM 
#     $a 
#     #t%
#     ^r!

matrix = [ 

    ["7", "i", "3"], 
    ["T", "s", "i"], 
    ["h", "%", "x"], 
    ["i", "#"," " ], 
    ["s", "M", " "], 
    ["$", "a", " "], 
    ["#", "t", "%"], 
    ["^", "r", "!"]  
]

regex = "[a-zA-Z]+"
col_list = []
for row in range(0, len(matrix[0])):
    for col, char  in enumerate(matrix):
        col_list.append(matrix[col][row])

str_matrix = "".join(col_list)
clean_matrix = re.findall(regex, str_matrix)
final_matrix = " ".join(clean_matrix) 
print(final_matrix)