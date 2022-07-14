# Instructions
# Write a program that accepts a comma separated sequence of words as input and prints the words in a comma-separated sequence after sorting them alphabetically.
# Use List Comprehension

# Example:
# Suppose the following input is supplied to the program: without,hello,bag,world
# Then, the output should be: bag,hello,without,world

user_input = input("Please enter a coma separated sentence ")
list_from_input = [word for word in user_input.split(",")]
list_from_input.sort()
string_from_list = ",".join(list_from_input)

print(string_from_list)