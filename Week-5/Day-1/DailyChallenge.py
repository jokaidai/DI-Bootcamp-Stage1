# Instructions : Old MacDonald’s Farm
# Take a look at the following code and output:
# File: market.py

# macdonald = Farm("McDonald")
# macdonald.add_animal('cow',5)
# macdonald.add_animal('sheep')
# macdonald.add_animal('sheep')
# macdonald.add_animal('goat', 12)
# print(macdonald.get_info())
# Output

# McDonald's farm

# cow : 5
# sheep : 2
# goat : 12

#     E-I-E-I-0!


# Create the code that is needed to receive the result provided above. Below are a few questions to assist you with your code:

# 1 - Create a class called Farm. How should it be implemented?
# 2 - Does the Farm class need an __init__ method? If so, what parameters should it take?
# 3 - How many methods does the Farm class need?
# 4 - Do you notice anything interesting about the way we are calling the add_animal method? What parameters should this function have? How many…?
# 5 - Test your code and make sure you get the same results as the example above.
#   Bonus: nicely line the text in columns as seen in the example above. Use string formatting.

# Expand The Farm
# Add a method called get_animal_types to the Farm class. This method should return a sorted list of all the animal types (names) in the farm. With the example above, the list should be: ['cow', 'goat', 'sheep'].
# Add another method to the Farm class called get_short_info. This method should return the following string: “McDonald’s farm has cows, goats and sheep.”. The method should call the get_animal_types function to get a list of the animals.

class Farm:
    """class that simulate the handling of a farm"""

    def __init__(self:object, owner:str, livestock = {"cow": 0, "sheep": 0, "goat": 0} ) -> object:

        self.owner = owner
        self.livestock = livestock


    def get_info(self:object) -> None:
        """a method that display the livestock in the farm"""
            
        for animal, num in self.livestock.items():
            print(f"{animal}: {num}")
        

    def get_short_info(self:object) -> None:
        """a method that use get_animal_types to get the animal available in livestock and display them in a fomated message"""

        short_info = self.get_animal_types()

        print(f"{self.owner}'s farm has {short_info[0]}s, {short_info[1]}s, and {short_info[2]}s.")


    def add_animal(self:object, animal:str, num_added = 1):
        """a method that allow the user to add animals to his livestock or increase the population of the existing ones increase by one by default"""
        if animal in self.livestock.keys():
            self.livestock[animal] += num_added
        else:
            print(f"Sorry {self.owner} you don't have those animals in stock just by one before starting adding them !!")


    def get_animal_types(self:object) -> list:
        """a method that create a list of the available livestock, sort it, and return it ... """

        type_list = []

        for animal in self.livestock.keys():
            type_list.append(animal)

        return type_list

macdonald = Farm("McDonald")
macdonald.add_animal('cow', 5)
macdonald.add_animal('sheep')
macdonald.add_animal('sheep')
macdonald.add_animal('goat', 12)
macdonald.get_info()
macdonald.get_short_info()