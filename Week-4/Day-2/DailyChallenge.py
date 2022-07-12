#CHALLENGE 1
# Instructions

# Ask the user for a number and a length.
# Create a program that prints a list of multiples of the number until the list length reaches length.
# Examples

# number: 7 - length 5 ➞ [7, 14, 21, 28, 35]

# number: 12 - length 10 ➞ [12, 24, 36, 48, 60, 72, 84, 96, 108, 120]

# number: 17 - length 6 ➞ [17, 34, 51, 68, 85, 102]

user_num = int(input("Choose a number please "))
user_len = int(input("Choose a length please "))
mutiply_table = []

for idx in range(1, user_len + 1):
    result = user_num * idx
    mutiply_table.append(result)

print(f"number: {user_num} - length {user_len} ==> {mutiply_table}")
#CHALLENGE 1

#CHALLENGE 2

# Write a program that asks a string to the user, and display a new string with any duplicate consecutive letters removed.
# Examples

# user's word : "ppoeemm" ➞ "poem"

# user's word : "wiiiinnnnd" ➞ "wind"

# user's word : "ttiiitllleeee" ➞ "title"

# user's word : "cccccaaarrrbbonnnnn" ➞ "carbon"

user_input = input("Write something with duplicate ")
list_from_input = list(user_input)
list_from_input = list(dict.fromkeys(list_from_input))
back_to_string = "".join(list_from_input)

print(f"users's word : {user_input} ==> {back_to_string}")

#CHALLENGE 2