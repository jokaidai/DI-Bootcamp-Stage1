# Exercise 1 : Family
# Instructions:
# 1 - Create a class called Family and implement the following attributes:
#   - members: list of dictionaries with the following keys : name, age, gender and is_child (boolean).
#   - last_name : (string)
# 
# 2 - Implement the following methods:
#   - # born: adds a child to the members list (use **kwargs), don’t forget to print a message congratulating the family.
#   - is_18: takes the name of a family member as a parameter and returns True if they are over 18 and False if not.
#   - family_presentation: a method that prints the family’s last name and all the members’ first name.

print("----- EX1 -----")

class Family():
    """
    this class is a family handler hold a list of familly member and allow action to modify the list
    """

    def __init__(self:object, members:list, last_name:str) -> object:
        
        self.members = members
        self.last_name = last_name


    def born(self:object, **baby) -> None:
        """
        get a new member from outside as a dict (**kwargs) add it to the members list and congratulate the family :)
        """
        
        self.members.append(baby)
     
        print(f"Congratulation for {baby['name']} birth !!!")


    def is_18(self:object,  member_name:str) -> bool:
        """
        get the name of one of the member from the list and check if he/she is 18 return true or false depending...
        """

        for member in self.members:
            if member_name == member['name']:
                if member['age'] >= 18:
                    return True

        return False

    
    def family_presentation(self:object):
        """
        print the family name and all of the members 
        """

        print(f"Welcome !!! take a look at the {self.last_name} family roster:")
        for member in self.members:
            print(member['name'])



bokobza = Family([
    {'name':'Michael', 'age':35, 'gender':'Male', 'is_child':False},
    {'name':'Sarah', 'age':32, 'gender':'Female', 'is_child':False}
 ], "Bokobza")

bokobza.born(name = "David", age = 0, gender = "Male", is_child = True)
bokobza.members[0]['age']
bokobza.family_presentation()

# Exercise 2 : TheIncredibles Family
# Instructions:
# 1 - Create a class called TheIncredibles. This class should inherit from the Family class:
#     -This is no random family they are an incredible family, therefore we need to add the following keys to our dictionaries: power and incredible_name.

# 2 - Add a method called use_power, this method should print the power of a member only if they are over 18 years old. If not raise an exception (look up exceptions) which stated they are not over 18 years old.

# 3 - Add a method called incredible_presentation which : * prints the family’s last name and all the members’ first name (ie. use the super() function, to call the family_presentation method) * prints all the members’ incredible name and power.

# 4 -  Call the incredible_presentation method.

# 5 -  Use the born method inherited from the Family class to add Baby Jack with the following power: “Unknown Power”.

# 6 -  Call the incredible_presentation method again.

print("----- EX2 -----")

class TheIncredible(Family):
    """
    this class is close to the family class with some modification ... its super hero family after all !!!
    """

    def __init__(self: object, members: list, last_name: str) -> object:
        super().__init__(members, last_name)


    def use_power(self:object, member:dict) -> None:
        """
        this method allow the use of power(print a nice message ...) only if the member is 18 
        """

        member_name = member['name']

        if self.is_18(member_name) == False:
            raise Exception("You still too young to be using your power young one !! remember we have to live in secret ...")
        else:
            print(f"{member_name} is using {member['power']}")

    def incredible_presentation(self:object):
        """
        overide of family_presentation of the family class to print 
        """

        super().family_presentation()

        print("but they are also known as:")
        for member in self.members:
            print(f"{member['incredible_name']}       power: {member['power']}")



incredible = TheIncredible([
    {'name':'Michael', 'age':35, 'gender':'Male', 'is_child':False, 'power': 'fly', 'incredible_name':'MikeFly'},
    {'name':'Sarah', 'age':32, 'gender':'Female', 'is_child':False, 'power': 'read minds', 'incredible_name':'SuperWoman'}
], "Parker")

for member in incredible.members:

    incredible.use_power(member)

incredible.incredible_presentation()

incredible.born(name ="Jackjack", age = 0, gender = "male", is_child = True, power = "Unknown Power ????", incredible_name = "EvilBaby") 
 
incredible.incredible_presentation()