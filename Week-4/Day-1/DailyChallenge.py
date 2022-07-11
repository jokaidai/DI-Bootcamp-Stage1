# Instructions
# Using the input function, ask the user for a string. The string must be 10 characters long.
# If it’s less than 10 characters, print a message which states “string not long enough”.
# If it’s more than 10 characters, print a message which states “string too long”.

# Then, print the first and last characters of the given text.

# Using a for loop, construct the string character by character: Print the first character, then the second, then the third, until the full string is printed. For example:
# The user enters "Hello World"
# Then, you have to construct the string character by character
# H
# He
# Hel
# ... etc
# Hello World


# 4. Bonus: Swap some characters around then print the newly jumbled string (hint: look into the shuffle method). For example:

# Hlrolelwod

user_string = input("Enter a phrase of 10 character min please (space count as a character)")
string_size = len(user_string)
if string_size < 10:
    print("Its too small try again please ")
elif string_size > 10:
    print("Its too long try again please")

print(user_string[0])
print(user_string[-1])

builder = " "
for character in range (string_size):
    builder += user_string[character]
    print(builder)

import random
char_list = list(user_string)
random.shuffle(char_list)
result = ''.join(char_list)
print(result)