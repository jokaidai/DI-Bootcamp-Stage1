import func
from datetime import date

# Exercise 1: Import
# Instructions:
# In a file named func.py create a function that adds 2 number, and prints the result
# In a file namedexercise_one.py import and the function

print("----- EX1 -----")

func.calc(5, 6)

# Exercise 2: Random Module
# Instructions:
# Create a function that accepts a number between 1 and 100, then rolls a random number between 1 and 100,
# if it’s the same number, display a success message to the user, else don’t.

print("----- EX2 -----")

func.compare_num(26)

# Exercise 3: String Module
# Instructions:
# Generate random String of length 5
# Note: String must be the combination of the UPPER case and lower case letters only. No numbers and a special symbol.
# Hint: use the string module

print("----- EX3 -----")

func.gen_string(5)

# Exercise 4 : Current Date
# Instructions:
# Create a function that displays the current date.
# Hint : Use the datetime module.

print("----- EX4 -----")

func.get_date()

# Exercise 5 : Amount Of Time Left Until January 1st
# Instructions:
# Create a function that displays the amount of time left from now until January 1st.
# (Example: the 1st of January is in 10 days and 10:34:01hours).

print("----- EX5 -----")

func.first_january()

# Exercise 6 : Birthday And Minutes
# Instructions:
# Create a function that accepts a birthdate as an argument (in the format of your choice), then displays a message stating how many minutes the user lived in his life.

print("----- EX6 -----")

func.calculate_age(date(1993, 3, 29))