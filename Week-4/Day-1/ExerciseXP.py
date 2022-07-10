#EX1
# #Instructions 
# Print Hello World in one line of code:

for message in range(5):
    print("Hello World")
#EX1

#EX2
#Instructions
# Write code that calculates the result of: (99^3) * 8 (99 to the power of 3 times 8)

print(99 ** 3 * 8)    
#EX2

#EX3
# Instructions
# Predict the output of the following code snippets:
#5 < 3  prediction:false  
#3 == 3  prediction:true  
#3 == "3"  prediction:false  
#"3" > 3  prediction:not supported  
#"Hello" == "hello" prediction:false  

#EX3

#EX4
# Instructions
# Create a variable called computer_brand which value is the brand name of your computer.
# Using the computer_brand variable print a sentence that states the following: "I have a <computer_brand> computer".

computer_brand = "DELL"
print(f"I have a {computer_brand} computer")
#EX4

#EX5
# Instructions
# Create a variable called name, and set it’s value to your name.
# Create a variable called age, and set it’s value to your age.
# Create a variable called shoe_size, and set it’s value to your shoe size.
# Create a variable called info and set it’s value to an interesting sentence about yourself. The sentence must contain all the variables created in parts 1, 2 and 3.
# Have your code print the info message.
# Run your code

name ="Elie"
age = 29
shoe_size = 44.5
print(f"My name is {name} i am {29} years old and my shoe size {shoe_size}!!! of course the last data is the most important because it's an hint that i want shoes for my anniversary gift !!! I love the jordan brand if you where wandering .... ")
#EX5

#EX6
# Instructions
# Create two variables, a and b.
# Each variable value should be a number.
# If a is bigger then b, have your code print Hello World.

a = 26
b = 13

if a > b:
    print("Hello World")
#EX6

#EX7
# Instructions
# Write code that asks the user for a number and determines whether this number is odd or even.

user_number = int(input("Choose a number"))
if user_number % 2 == 0:
    print("Your number is even")
else: 
    print("Your number is odd")

#EX7

#EX8
# Instructions
# Write code that asks the user for their name and determines whether or not you have the same name, print out a funny message based on the outcome.

my_name ="Elie"
user_name = input("What is your name ?")

if my_name == user_name:
    print(f"You are the man {user_name} ;)")
else:
    print("WHAT ARE YOU EVEN TALKING TO ME FOR YOU PEASANT GET LOST !!!")

#EX8

#EX9s
# Instructions
# Write code that will ask the user for their height in inches.
# If they are over 145cm print a message that states they are tall enough to ride.
# If they are not tall enough print a message that says they need to grow some more to ride.

user_height = float(input("What is your height in inches please."))
if user_height >= 57.0866:
    print("You are tall enough to ride congratulation")
else:
    print("You are not quite there yet, you need to grow some more..")
#EX9