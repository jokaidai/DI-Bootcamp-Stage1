import random

# EXERCISE 1: What Are You Learning ?
# Instructions:

# 1 - Write a function called display_message() that prints one sentence telling everyone what you are learning in this course.

# 2 - Call the function, and make sure the message displays correctly.

print("-----EX1-----")

def display_message() -> None:
    """First function that print my formation and dream !!"""

    print("Hi everyone !!!! I am here to learn to become a full stack developer and I hope that someday I can become a game designer !!! :P")

display_message()

# EXERCISE 2: What’s Your Favorite Book ?
# Instructions:

# 1 - Write a function called favorite_book() that accepts one parameter called title.

# 2 - The function should print a message, such as "One of my favorite books is <title>".
#   For example: “One of my favorite books is Alice in Wonderland”

# 3 - Call the function, make sure to include a book title as an argument when calling the function. 

print("-----EX2-----")

def favorite_book(title: str) -> None:
    """print what my favorite book is ..."""

    print(f"My favorite book is {title} !!!")

favorite_book("Harry Potter")

# EXERCISE 3 : Some Geography
# Instructions:

# 1 - Write a function called describe_city() that accepts the name of a city and its country as parameters.

# 2 - The function should print a simple sentence, such as "<city> is in <country>".
#   For example “Reykjavik is in Iceland”

# 3 - Give the country parameter a default value.

# 4 - Call your function.

print("-----EX3-----")

def describe_city(city: str, country = "France") -> None:
    """print a message that combine the two str (a city and a country) that the user choose """

    print(f"{city} is in {country}")

describe_city("london", "UK")

# EXERCISE 4 : Random
# Instructions:

# 1 - Create a function that accepts a number between 1 and 100 and generates another number randomly between 1 and 100.

# 2 - Compare the two numbers, if it’s the same number, display a success message, otherwise show a fail message and display both numbers

print("-----EX4-----")

def guess_my_num(player_num: int) -> None:
    """a function that generate a random num from 1 to 100 and compare it to the num in the parameter"""

    ai_num = random.randint(1, 100)
    if player_num == ai_num:
        print("You guessed my number !!!! how did you dooo ????")
    else:
        print(f"your num: {player_num} ---- my num: {ai_num}")
        print("you failed miserably ....")

guess_my_num(26)

# EXERCISE 5 : Let’s Create Some Personalized Shirts !
# Instructions:

# 1 - Write a function called make_shirt() that accepts a size and the text of a message that should be printed on the shirt.

# 2 - The function should print a sentence summarizing the size of the shirt and the message printed on it, such as "The size of the shirt is <size> and the text is <text>"

# 3 - Call the function make_shirt().

# 4 - Modify the make_shirt() function so that shirts are large by default with a message that reads “I love Python” by default.

# 5 - Make a large shirt with the default message

# 6 - Make medium shirt with the default message

# 7 -Make a shirt of any size with a different message.

# Bonus: Call the function make_shirt() using keyword arguments.

print("-----EX5-----")

def make_shirt(size = "L", message = "I love Python" ) -> None:
    """function that make t shirts according to the specificity off the caller or refer to default tshirt if not specify"""

    print(f"The size of the shirt is {size} and the text is {message}")

make_shirt("XL", "while(alive) {code(); eat(); repeat;}")
make_shirt()
make_shirt("M")
make_shirt(message = "Winter is comming", size = " XXL")

# EXERCISE 6 : Magicians …
# Instructions:

# 1 - Using this list of magician’s names. magician_names = ['Harry Houdini', 'David Blaine', 'Criss Angel']

# 2 - Pass the list to a function called show_magicians(), which prints the name of each magician in the list.

# 3 - Write a function called make_great() that modifies the list of magicians by adding the phrase "the Great" to each magician’s name.

# 4 - Call the function make_great().

# 5 - Call the function show_magicians() to see that the list has actually been modified.

print("-----EX6-----")

magician_names = ['Harry Houdini', 'David Blaine', 'Criss Angel']

def show_magicians(list: list) -> None :
    """a fucntion that loop from the list in parameter and print the data inside the list"""

    for name in list:
        print(name)

def make_great(list: list) -> list:
    """a funct that modify every data inside the parameter's list and add the great at the beginning"""

    great_list =  ["the Great " + name for name in list]
    return great_list

show_magicians(magician_names)

magician_names= make_great(magician_names)
show_magicians(magician_names)

# EXERCISE 7 : Temperature Advice
# Instructions:

# 1 - Create a function called get_random_temp().
#   1 - This function should return an integer between -10 and 40 degrees (Celsius), selected at random.
#   2 - Test your function to make sure it generates expected results.

# 2 - Create a function called main().
#   1 - Inside this function, call get_random_temp() to get a temperature, and store its value in a variable.
#   2 - Inform the user of the temperature in a friendly message, eg. “The temperature right now is 32 degrees Celsius.”

# 3 - Let’s add more functionality to the main() function. Write some friendly advice relating to the temperature:
#   1 - below zero (eg. “Brrr, that’s freezing! Wear some extra layers today”)
#   2 - between zero and 16 (eg. “Quite chilly! Don’t forget your coat”)
#   3 - between 16 and 23
#   4 - between 24 and 32
#   5 - between 32 and 40

# 4 - Change the get_random_temp() function:
#   1 - Add a parameter to the function, named ‘season’.
#   2 - Inside the function, instead of simply generating a random number between -10 and 40, set lower and upper limits based on the season, eg. if season is ‘winter’, temperatures should only fall between -10 and 16.
#   3 - Now that we’ve changed get_random_temp(), let’s change the main() function:
#       1 - Before calling get_random_temp(), we will need to decide on a season, so that we can call the function correctly. Ask the user to type in a season - ‘summer’, ‘autumn’ (you can use ‘fall’ if you prefer), ‘winter’, or ‘spring’.
#       2 - Use the season as an argument when calling get_random_temp().

# Bonus: Give the temperature as a floating-point number instead of an integer.
# Bonus: Instead of asking for the season, ask the user for the number of the month (1 = January, 12 = December). Determine the season according to the month.

print("-----EX7-----")

def get_random_temp(season: str) -> int :
    """this function return a random num according to the season var"""

    if season == "winter" :
        celsius = random.randint(-10, 16)
        return celsius 
    
    elif season == "spring" :
        celsius = random.randint(21, 32)
        return celsius
    
    elif season == "summer" :
        celsius = random.randint(32, 40)
        return celsius
    
    elif season == "autumn" :
        celsius = random.randint(16, 21)
        return celsius

def get_month() -> str:
    """utility function to get the month for the user""" 

    month = 0
    while not (1 <= month <= 12):
       
        month = int(input("What is the number of the month ??"))

        if  3 <= month <= 5:
            season = "spring"
    
        elif  6 <= month <= 8:
            season = "summer"
    
        elif  9 <= month <= 11:
            season = "autumn"
    
        else:
            season = "winter"
    
    return season

def main() -> None:
    """main fuction for the moment print a message using get_random_temp funct"""

    season = get_month()

    celsius = get_random_temp(season)
    if celsius <= 0:
        print(f"The temperature right now is {celsius} degrees Celsius.Brrr, that's freezing! Wear some extra layers today")
   
    elif 0 < celsius <= 16:
        print(f"The temperature right now is {celsius} degrees Celsius.Brrr, Quite chilly! Don't forget your coat")
    
    elif 16 < celsius <= 23:
        print(f"The temperature right now is {celsius} degrees Celsius.A bit windy but you should get some sun !!")
    
    elif 23 < celsius <= 32:
        print(f"The temperature right now is {celsius} degrees Celsius.No clouds in the sky !!! Enjoy")
    
    elif 32 < celsius <= 40:
        print(f"The temperature right now is {celsius} degrees Celsius.It's hell 's heat out here !!!! stay near an A.C !! friend advice ;)")

main()