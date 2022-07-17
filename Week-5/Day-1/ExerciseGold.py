import math
import random

# Exercise 1 : Geometry
# Instructions:

# 1 - Write a class called Circle that receives a radius as an argument (default is 1.0).
# 2 - Write two instance methods to compute perimeter and area.
# 3 - Write a method that prints the geometrical definition of a circle.

class Circle:
    """a class that emulate a circle and his basic operations"""

    def __init__(self:object, radius = 1.0) -> object:
        self.radius = radius


    def compute_perimeter(self:object) -> float:
        """a method that compute the perimeter of the circle and return it """

        perimeter = math.pi * 2 * self.radius

        return perimeter
    

    def compute_area(self:object) -> float:
        """a method that compute the area of the circle and return it """
        
        radius_for_area = pow(self.radius, 2)
        area = math.pi * radius_for_area

        return area

    
    def definition(self:object) -> None:
        """"a method that simply print the geometrical definition of a circle"""

        print("A circle is the set of all points in the plane that are a fixed distance (the radius) from a fixed point (the centre). Any interval joining a point on the circle to the centre is called a radius. By the definition of a circle, any two radius have the same length.")

        
        
# Exercise 2 : Custom List Class
# Instructions:

# 1 - Create a class called MyList, the class should receive a list of letters.
# 2 - Add a method that returns the reversed list.
# 3 - Add a method that returns the sorted list.
#   Bonus : Create a method that generates a second list with the same length as mylist. The list should be constructed with random numbers. (use list comprehension).

class MyList ():
    """a class that creates holding list 's object and allow some action on them """

    def __init__(self:object, letter_list:list) -> object:
        
        self.letter_list = letter_list

    
    def reverse_it(self:object) -> None:
        """this method reverse the list hold by the object and return it"""

        reverted_list = reversed(self.letter_list)

        return list(reverted_list)
        

    def sort_it(self:object) -> None:
        """this method sort the list hold by the object and return it"""

        sorted_list = sorted(self.letter_list)

        return list(sorted_list)

    
    def create_new_list(self:object) -> None:
        """this method create a new list ussing the length of the one already created, fill it with numbers and return it """

        new_list = [random.randint(0, 100) for num in range (len(self.letter_list))]

        return  new_list
        

       


list1 = MyList(["E", "I", "L", "E"])
print(list1.letter_list)
print(list1.reverse_it())
print(list1.sort_it())
list2 = list1.create_new_list()
print(list2)