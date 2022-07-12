#CHALLENGE 1
#INSTRUCTIONS:

# 1- Ask a user for a word
# 2- Write a program that creates a dictionary. This dictionary stores the indexes of each letter in a list.

#   Make sure the letters are the keys.
#   Make sure the letters are strings.
#   Make sure the indexes are stored in a list and those lists are values.
#   
#   Examples:

# "dodo" ➞ { "d": [0, 2], "o": [1, 3] }

# "froggy" ➞ { "f":  [0], "r": [1], "o": [2], "g": [3, 4], "y": [5] }

# "grapes" ➞ { "g": [0], "r": [1], "a": [2], "p": [3]}

user_word = str(input("Gimme a word !!"))
user_word_char_list = list(user_word)

user_word_idx_list = []
for idx, letter in enumerate(user_word_char_list):
    user_word_idx_list.append(idx)
    
print(user_word_idx_list)

# dict_from_user_word = dict(zip(user_word_char_list, user_word_idx_list))
# print(dict_from_user_word)