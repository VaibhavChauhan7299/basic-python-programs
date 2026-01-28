#OOP
# To map with real world scenarios, we started using objects in code.
# This is called object oriented programming.


# Class & Objects
# Class is a blueprint for creating objects.
#The self parameter is a reference to the current instance of the class,  and is used to access variables that belongs to the class.

class Students :
    name = "karan"
    def __init__(self, fullname,):
        self.name = fullname
        print("adding new student in Database..")
       
s1 = Students("vaibhav")
print(s1.name)

s2 = Students("yashvi")
print(s2.name)

# class Car:
#     color = "Blue"
#     brand = "mercedes"

# Car1 = Car()
# print(Car1.color)        
# print(Car1.brand)

#_ _init_ _ function

#Constructor:
# All classes have a function called_init_(), which is always executed when the class is being intiated.