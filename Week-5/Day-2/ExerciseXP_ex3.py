from ExerciseXP import Dog 
import random

# Exercise 3 : Dogs Domesticated
# Instructions:
# 1 - Create a new python file and import your Dog class from the previous exercise.
# 2 - In the new python file, create a class named PetDog that inherits from Dog.
# 3 - Add an attribute called trained to the __init__ method, this attribute is a boolean and the value should be False by default.
# 4 - Add the following methods:
#       -train: prints the output of bark and switches the trained boolean to True
#       -play: takes a parameter which value is a few names of other Dog instances (use *args). The method should print the following string: “dog_names all play together”.
#       -do_a_trick: If the dog is trained the method should print one of the following sentences at random:
#           -“dog_name does a barrel roll”.
#           -“dog_name stands on his back legs”.
#           -“dog_name shakes your hand”.
#           -“dog_name plays dead”.

class PetDog(Dog):
    """
    a class that inherit from the dog class and add new possibilities
    """

    def __init__(self: object, name: str, age: int, weight: int, trained = False) -> object:
        super().__init__(name, age, weight)
        self.trained = trained

    def train(self:object) -> None:
        self.bark()
        self.trained = True
    
    def play(self:object, *dogs:object) -> None:
        print(f"{dogs} all play together")
    
    def do_a_trick(self:object) -> None:
        trick_list = [f"{self.name} does a barrel roll", f"{self.name} stand on his back leg", f"{self.name} shake your hand", f"{self.name} play dead"]
        trick = random.randchoice(trick_list)

        if self.trained == True:
            print(trick)

columbus = PetDog("Columbus", 8, 10)
columbus.train()