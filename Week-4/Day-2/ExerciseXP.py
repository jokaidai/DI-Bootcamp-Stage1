#EX1
# Instructions

# Create a set called my_fav_numbers with all your favorites numbers.
# Add two new numbers to the set.
# Remove the last number.
# Create a set called friend_fav_numbers with your friend’s favorites numbers.
# Concatenate my_fav_numbers and friend_fav_numbers to a new variable called our_fav_numbers.

from tabnanny import check
from tkinter import FALSE


my_fav_numbers = {7, 13, 26}
my_fav_numbers.add(52)
my_fav_numbers.add(78)
print(my_fav_numbers)
my_fav_numbers.pop()
print(my_fav_numbers)

lisa_fav_numbers = {39, 41, 900}

our_fav_numbers = my_fav_numbers.union(lisa_fav_numbers)
print(our_fav_numbers)
#EX1

#EX2
# Instructions

# Given a tuple which value is integers, is it possible to add more integers to the tuple?
# # answer : its depend because Tuples are immutable lists, which means items can’t be changed.
# but you can create a new Tuple with the things you want to add... for exemple :

tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
tuple1 += tuple2

print(tuple1)
#EX2

#EX3
# Instructions

# Using this list basket = ["Banana", "Apples", "Oranges", "Blueberries"];
# Remove “Banana” from the list.
# Remove “Blueberries” from the list.
# Add “Kiwi” to the end of the list.
# Add “Apples” to the beginning of the list.
# Count how many apples are in the basket.
# Empty the basket.
# Print(basket)

basket = ["Banana", "Apples", "Oranges", "Blueberries"]
basket.remove("Banana")
print(basket)
basket.remove("Blueberries")
print(basket)
basket.append("kiwi")
print(basket)
basket.insert(0, "Apples")
print(basket)
print(basket.count("Apples"))
basket.clear()
print(basket)
#EX3

#EX4
# Instructions

# 1-Recap – What is a float? What is the difference between an integer and a float?
# 2-Can you think of another way to generate a sequence of floats?
# 3-Create a list containing the following sequence 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5 (don’t hard-code the sequence).

# answer:
# 1- float take decimal number int don't.
# 2-you can generate it float by playing with the for range loop like this:

start = 15
stop = 55
step = 5
float_list = []
print("range of float number :")
for val in range(start, stop, step):
    float_list.append(val / 10)
print (float_list)
#EX4

#EX5
# Instructions

# Use a for loop to print all numbers from 1 to 20, inclusive.
# Using a for loop, that loops from 1 to 20(inclusive), print out every element which has an even index. 


for counter in range(0, 21):
    print(counter)

for idx, num in enumerate(range(1, 21)):
    if(idx % 2 == 0):
        print(f"{num} have an even index:{idx}") 
#EX5

#EX6
# Instructions

# Write a while loop that will continuously ask the user for their name, unless the input is equal to your name.

my_name = "Elie"
while True:
    user_name = input("What is your name ? ")
    if(user_name == my_name):
        break    
#EX6

#EX7
# Instructions

# Ask the user to input their favorite fruit(s) (one or several fruits).
# Hint : Use the built in input method. Ask the user to separate the fruits with a single space, eg. "apple mango cherry".
# Store the favorite fruit(s) in a list (convert the string of words into a list of words).
# Now that we have a list of fruits, ask the user to input a name of any fruit.
# If the user’s input is in the favorite fruits list, print “You chose one of your favorite fruits! Enjoy!”.
# If the user’s input is NOT in the list, print, “You chose a new fruit. I hope you enjoy”.

user_favFruits = input("Type your favorite fruits (please separate each one with a space) ")
favFruit_list = user_favFruits.split()
print (favFruit_list)
user_fruit = input ("What fruit would you like right now ?")

if user_fruit in user_favFruits:
    print("You chose one of your favorite fruits! Enjoy!")
else:
    print("You chose a new fruit. I hope you enjoy")
#EX7

#EX8
# Instructions

# Write a loop that asks a user to enter a series of pizza toppings, when the user inputs ‘quit’ stop asking for toppings.
# As they enter each topping, print a message saying you’ll add that topping to their pizza.
# Upon exiting the loop print all the toppings on the pizza pie and what the total price is (10 + 2.5 for each topping).

active = True
price = 10
topping_added = ""

while active: 
    topping = input("Please enter the topping you would like in your Pizza (enter 'quit' when you are finished): ")
    if topping == 'quit':
        active = False
    else:
        print(f"You added {topping} to your Pizza !")
        price += 2.5
        topping_added += topping + " "

if topping_added == "":
    topping_added = "nothing"

print(f"you added {topping_added} to you Pizza the final check is {price}$")
#EX8

#EX9
# Instructions

# A movie theater charges different ticket prices depending on a person’s age.
# if a person is under the age of 3, the ticket is free.
# if they are between 3 and 12, the ticket is $10.
# if they are over the age of 12, the ticket is $15.
# Ask a family the age of each person who wants a ticket.
# Store the total cost of all the family’s tickets and print it out.

# A group of teenagers are coming to your movie theater and want to watch a movie that is restricted for people between the ages of 16 and 21.
# Given a list of names, write a program that asks teenager for their age, if they are not permitted to watch the movie, remove them from the list.
# At the end, print the final list.

family_size = int(input("How many tickets do you want ? "))
price = 0
while True: 
    
    if family_size == 0:
        break
    else:
       famMember_age =  int(input("How old are you ?"))

    if famMember_age < 3:
        print("next ")
        family_size -= 1 

    elif  3 <= famMember_age <= 12:
        price += 10 
        print("next ")
        family_size -= 1 

    elif famMember_age > 12:
        price += 15 
        print("next ")
        family_size -= 1 

print(f"{price}$ please :) ")

teen_names = input("What are your names ? ")
teen_list = teen_names.split()
# group_size = len(teen_list)
print(teen_list)

for idx, teen in enumerate(teen_list):
    
    teen_age = int(input(f"{teen} How old are you ?"))
    if 16 < teen_age < 21:
        del teen_list[idx]
        print("Sorry you are not permited to watch this movie :( ")
    else:
        print("Enjoy !! :)")    
print(teen_list)
#EX9
#EX10
# Instructions

# Use the above list called sandwich_orders.
# Make an empty list called finished_sandwiches.
# As each sandwich is made, move it to the list of finished sandwiches.
# After all the sandwiches have been made, print a message listing each sandwich that was made , such as I made your tuna sandwich.

sandwich_orders = ["Tuna sandwich", "Avocado sandwich", "Egg sandwich", "Sabih sandwich", "Pastrami sandwich"]
finished_sandwiches = []

for sandwich in sandwich_orders:
    finished_sandwiches.append(sandwich)

for sandwich in finished_sandwiches:
    print(f"I made your {sandwich} !!")
#EX10

#EX11
# Instructions

# Using the list sandwich_orders from the previous exercise, make sure the sandwich ‘pastrami’ appears in the list at least three times.
# Add code near the beginning of your program to print a message saying the deli has run out of pastrami, and then use a while loop to remove all occurrences of ‘pastrami’ from sandwich_orders.
# Make sure no pastrami sandwiches end up in finished_sandwiches.

print ("sorry but the deli run out of pastrami :(")

unwanted_sandwich ="Pastrami sandwich"
for sandwich in sandwich_orders:
    finished_sandwiches.append(sandwich)
    if(sandwich == unwanted_sandwich ):
        finished_sandwiches.append(sandwich)
        finished_sandwiches.append(sandwich)

while unwanted_sandwich in finished_sandwiches:
    finished_sandwiches.remove(unwanted_sandwich)

for sandwich in finished_sandwiches:
    print(f"I made your {sandwich} !!")
#EX11