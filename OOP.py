#OOP
# To map with real world scenarios, we started using objects in code.
# This is called object oriented programming.


# Class & Objects
# Class is a blueprint for creating objects.
#The self parameter is a reference to the current instance of the class,  and is used to access variables that belongs to the class.

# class Students1:
#     name = "karan"
# s1 = Students1()
# print(s1.name)

# class Car:
#     color = "Blue"
#     brand = "mercedes"

# Car1 = Car()
# print(Car1.color)        
# print(Car1.brand)

#_ _init_ _ function

#Constructor:
# All classes have a function called_init_(), which is always executed when the class is being intiated.

#The self parameter is a reference to the current instance of the class, and is used to access variables that belongs to the class.

#there are two types of construtors 1- default constructors, 2- parameterized constructors.
# class Students :

#     def __init__(self, name, marks):
#         self.name = name
#         self.marks = marks
#         print("adding new student in Database..")
       
# s1 = Students("vaibhav", 97)
# print( s1.name, s1.marks)

# s2 = Students("yashvi", 99)
# print(s2.name, s2.marks)

# attributes ---> data;variables

#class & instance Attributes

#1 = Class.attr
#2 = obj.attr

class Students :
    college_name = "RK university"
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
        print("adding new student in Database..")
       
s1 = Students("vaibhav", 97)
print( s1.name, s1.marks)
print(s1.college_name)

s2 = Students("yashvi", 99)
print(s2.name, s2.marks)
print(s2.college_name)