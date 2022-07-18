#EX1 Pets
#INSTRUCTIONS:
# 1 - Create another cat breed named Siamese which inherits from the Cat class.
# 2 - Create a list called all_cats, which holds three cat instances : one Bengal, one Chartreux and one Siamese.
# 3 - Those three cats are Sara’s pets. Create a variable called sara_pets which value is an instance of the Pet class, and pass the variable all_cats to the new instance.
# 4 - Take all the cats for a walk, use the walk method.

print("----- EX1 -----")

class Pets():
    """
    a class that create pet with the basic walk() method
    """

    def __init__(self:object, animals:list) -> object:
        self.animals = animals

    def walk(self):
        for animal in self.animals:
            print(animal.walk())

class Cat():

    is_lazy = True

    def __init__(self:object, name:str, age:int) -> object:
        self.name = name
        self.age = age

    def walk(self):
        return f'{self.name} is just walking around'

class Bengal(Cat):
    def sing(self:object, sounds:str):
        return f'{sounds}'

class Chartreux(Cat):
    def sing(self:object, sounds:str):
        return f'{sounds}'

class Siamese(Cat):
    def sing(self:object, sounds:str):
        return f'{sounds}'

beny = Bengal("Benny", 4)
charly = Chartreux("Charly", 6)
sia = Siamese("Sia", 2)

all_cats = [beny, charly, sia]

sara_pets = Pets(all_cats)
sara_pets.walk()

# Exercise 2 : Dogs
# Instructions:
# 1 - Create a class called Dog with the following attributes name, age, weight.
# 2 - Implement the following methods in the Dog class:
#       bark: returns a string which states: “<dog_name> is barking”.
#       run_speed: returns the dogs running speed (weight/age*10).
#       fight : takes a parameter which value is another Dog instance, called other_dog. This method returns a string stating which dog won the fight. The winner should be the dog with the higher run_speed x weight.

# 3 - Create 3 dogs and run them through your class.

print("----- EX2 -----")

class Dog():

    def __init__(self:object, name:str, age:int, weight:int) -> object:
        self.name = name
        self.age = age
        self.weight = weight


    def bark(self:object) -> None:

        print(f"{self.name} is barking")


    def run_speed(self:object) -> int:

        return self.weight / self.age * 10


    def fight(self:object, other_dog:object) -> str:

        winner = " "

        if self.run_speed() > other_dog.run_speed():
            winner = self.name
        else:
            winner = other_dog.name
        
        return winner

    
cerberus = Dog("Cerberus", 5, 19)
varen = Dog("Varen", 18, 12)
lady = Dog("Lady", 4, 6)

print("----- Cerberus -----")
cerberus.bark()
print((f"The winner is : {cerberus.fight(varen)}"))
print((f"The winner is : {cerberus.fight(lady)}"))

print("----- Varen -----")
varen.bark()
print((f"The winner is : {varen.fight(cerberus)}"))
print((f"The winner is : {varen.fight(lady)}"))

print("----- Lady -----")
lady.bark()
print((f"The winner is : {lady.fight(cerberus)}"))
print((f"The winner is : {lady.fight(varen)}"))


