#EX1
#INSTRUCTIONS:

# 1 - Instantiate three Cat objects using the code provided above.
# 2 - Outside of the class, create a function that finds the oldest cat and returns the cat.
# 3 - Print the following string: “The oldest cat is <cat_name>, and is <cat_age> years old.”. Use the function previously created.

print("----- EX1 -----")

class Cat:

    cats = []

    def __init__(self, cat_name:str, cat_age:int) -> object:
        self.name = cat_name
        self.age = cat_age

        Cat.cats.append(self)

cat1 = Cat("Rajah", 12)
cat1 = Cat("Bagerah", 20)
cat1 = Cat("Simba", 5)

def find_older(cats:list) -> object:
    """a function that compare the age of the cat and return the oldest"""

    older = cats[0]
    for cat in cats:
        if cat.age > older.age:
            older = cat

    return older

older = find_older(Cat.cats)
print(f"The oldest cat is {older.name} and is age is {older.age} !!!")

#EX2
#INSTRUCTIONS:
# 1 - Create a class called Dog.
# 2 - In this class, create an __init__ method that takes two parameters : name and height. This function instantiates two attributes, which values are the parameters.
# 3 - Create a method called bark that prints the following string “<dog_name> goes woof!”.
# 4 - Create a method called jump that prints the following string “<dog_name> jumps <x> cm high!”. x is the height*2.
# 5 - Outside of the class, create an object called davids_dog. His dog’s name is “Rex” and his height is 50cm.
# 6 - Print the details of his dog (ie. name and height) and call the methods bark and jump.
# 7 - Create an object called sarahs_dog. Her dog’s name is “Teacup” and his height is 20cm.
# 8 - Print the details of her dog (ie. name and height) and call the methods bark and jump.
# 9 - Create an if statement outside of the class to check which dog is bigger. Print the name of the bigger dog.

print("----- EX2 -----")

class Dog:

    dogs = []

    def __init__(self, dog_name:str, height: int) -> object:
        self.name = dog_name
        self.height = height

        Dog.dogs.append(self)

    def print_detail(self:object) -> None:
        """a function that print the detail of the dog"""

        print(f"My dog name is {self.name}!! And he is {self.height}cm tall.")

    
    def bark(self:object) -> None:
        """function that make the dog bark !!!"""

        print(f"{self.name} goes woof!")

    def jump(self:object) -> None:
        """function that make the dog jump !!!"""
        
        print(f"{self.name} jumps {self.height * 2} cm high!")

def find_biger(dogs:list) -> object:
    """a function that compare the age of the cat and return the oldest"""

    biger = dogs[0]
    for dog in dogs:
        if dog.height > biger.height:
            biger = dog

    return biger

    
davids_dog = Dog("Rex", 50)
davids_dog.print_detail()
davids_dog.bark()
davids_dog.jump()

sarahs_dog = Dog("Teacup", 20)
sarahs_dog.print_detail()
sarahs_dog.bark()
sarahs_dog.jump()

biger = find_biger(Dog.dogs)
print((f"The biger dog is {biger.name} !!"))

#EX3
#INSTRUCTIONS:
# 1 - Define a class called Song, it will show the lyrics of a song.
# 2 - Its __init__() method should have two arguments: self and lyrics (a list).
# 3 - Inside your class create a method called sing_me_a_song that prints each element of lyrics on its own line.
# 4 - Then, call the sing_me_a_song method.

print("----- EX3 -----")

class Song:
    """a class that stock the lyrics of a song """

    def __init__(self:object, lyrics:list ) -> object:
        self.lyrics = lyrics

    def sing_me_a_song(self:object) -> None:
        """a function to emulate the computer singing !!! it read the sentences from the lyrics list one by one and display them """

        for sentence in self.lyrics:
            print(sentence)

just_the_two_of_us = Song(["I see the crystal raindrops fall", "And the beauty of it all", "Is when the sun comes shining through", "To make those rainbows in my mind", "When I think of you sometime", "And I wanna spend some time with you"])

just_the_two_of_us.sing_me_a_song()

#EX4
#INSTRUCTIONS:
# 1 - Create a class called Zoo.
# 2 - In this class create a method __init__ that takes one parameter: zoo_name.
# 3 - It instantiates two attributes: animals (an empty list) and name (name of the zoo).
# 4 - Create a method called add_animal that takes one parameter new_animal. This method adds the new_animal to the animals list as long as it isn’t already in the list.
# 5 - Create a method called get_animals that prints all the animals of the zoo.
# 6 - Create a method called sell_animal that takes one parameter animal_sold. This method removes the animal from the list and of course the animal needs to exist in the list.
# 7 - Create a method called sort_animals that sorts the animals alphabetically and groups them together based on their first letter.
# 8 - Create a method called get_groups that prints the animal/animals inside each group.
# 9 - Create an object called ramat_gan_safari and call all the methods.
#       Tip: The zookeeper is the one who will use this class.

print("----- EX4 -----")

class Zoo:
    """a class that old the name of the zoo and each animals in it"""

    def __init__(self, zoo_name:str, animals:list) -> object:
        self.zoo_name = zoo_name
        self.animals = animals
    
    def add_animal(self:object, new_animal:str) -> None:
        """a method that check if an animal is present in the zoo and add it if he is not """

        if new_animal not in self.animals:
            self.animals.append(new_animal)
        
        else:
            print(f"We already have those in {self.zoo_name} but thanks")
    
    def get_animals(self:object) -> None:
        """a method that display all the animal present in the zoo"""

        for animal in self.animals:
            print(animal)

    def sell_animal(self:object, sold_animal) -> None:
        """a method that check if an animal is present in the zoo and remove it if he is"""

        if sold_animal in self.animals:
           self.animals.remove(sold_animal)
        else:
            print("Sorry we don't have this animal you are looking for ... ")

    def sort_animals(self:object) -> dict:
        """this method sort alphabeticaly the animals of the list and group them by first letter of the name inside a dictionary ..."""

        sorted_animals = sorted(self.animals)
        grouped_animals = {}

        for animal in sorted_animals:
             if animal[0] not in grouped_animals:
                grouped_animals[animal[0]] = [animal]
        
             else:
                grouped_animals[animal[0]].append(animal)
        
        return grouped_animals

    def get_groups(self:object) -> None:
        """this method print the animal in the zoo sorted by alphabetical group"""

        to_print = self.sort_animals()

        print(to_print)

ramat_gan_safari = Zoo("Ramat Gan Safari", ["Wolfs", "Gorillas", "Giraffes", "Monkeys", "Alpaccas", "Aligators", "Snakes"])

ramat_gan_safari.get_animals()
print("---------")
ramat_gan_safari.add_animal("Lions")
ramat_gan_safari.sell_animal("Wolfs")
ramat_gan_safari.get_animals()
print("---------")
ramat_gan_safari.get_groups()