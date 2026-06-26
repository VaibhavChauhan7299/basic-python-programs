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

# class Students :
#     college_name = "RK university"
#     def __init__(self, name, marks):
#         self.name = name #obj attr > classs attr
#         self.marks = marks
#         print("adding new student in Database..")

#     def welcome(self):
#          print("welcome student", self.name)    

#     def get_marks(self):
#         return self.marks     
       
# s1 = Students("vaibhav", 97)
# s1.welcome()
# print( s1.name, s1.marks)
# print(s1.college_name)
# print(s1.get_marks())


# s2 = Students("yashvi", 99)
# print(s2.name, s2.marks)
# print(s2.college_name)

#methods: Methods are functions that belong to objects

# def welcome(self):
#     print("welcome students")

# create student class that takes name & marks of 3 subjects as arguments in constructor. Then create a method to print the average.

# class Students:

#     def __init__(self, name, marks):
#         self.name = name 
#         self.marks = marks

#     @staticmethod
#     def hello():
#         print("hello")

#     def get_avg(self):
#         sum = 0
#         for val in self.marks:
#             sum += val
#         print("Hi", self.name, "your avg score is:", sum/3)

# s1 = Students("vaibhav", [99,97,98])
# s1.get_avg()        
# s1.hello()
#Static Methods: Methods that don't use the self parameter(work at class level)

#decorators allows us to wrap another function in order to extend the behaviour of the wrapped function, without permanently modifying it.

#OOP Structure is in 4 pillars:

#1 Abstaction: Hiding the implementation details of a class and only showing the essential features to the user.

#ex:

# class Car:
#     def __init__(self):
#         self.acc = False
#         self.brk = False
#         self.clutch = False

#     def start(self):
#         self.clutch = True    
#         self.acc = True
#         print("car started..")

# car1 = Car()
# car1.start()


#2 Encapsulation: wrapping data and functions into a single unit (object).

#question: Create Account class with 2 attributes - balance & account no. .Create a method to deposit and withdraw money from the account.

# class Account:
#     def __init__ (self, bal, acc):
#         self.balance = bal
#         self.account_no = acc

#     def debit(self, amount):
#         self.balance -= amount
#         print("Rs. ", amount, "was debited")
#         print("total balance =", self.get_balance())



#     def credit(self, amount):
#         self.balance += amount
#         print("Rs. ", amount, "was credited")
#         print("total balance =", self.get_balance())


#     def get_balance(self):
#         return self.balance        
    
# acc1 = Account (10000, 12345) 
# # print(acc1.balance)
# # print(acc1.account_no)   
# acc1.debit(5000)
# acc1.credit(2000)
# acc1.credit(55000)


# del keyword: used to delete object properties or object itself.
#del s1.name
#del s1

#ex

# class Students:
#     def __init__(self, name):
#         self.name = name

# s1 = Students("vaibhav")
# print(s1.name)
# del s1.name
# print(s1.name)        

#private attributes & methods:
#Conceptual Implementations in python : private attributes & methods are meant to be used only within the class and are not accessible from outside the class.
# ex

# class Account:
#     def __init__(self, acc_no, acc_pass):
#         self.acc_no = acc_no
#         self.__acc_pass = acc_pass

#     def reset_pass(self):
#         print(self.__acc_pass)    

# acc1 = Account("12345", "abc@123")

# print(acc1.acc_no)
# print(acc1.reset_pass()

#Inheritance:
# When one class(child/derived) derives the properties & methods of another class9parent/base).
#TYPES OF INHERITANCE:
#1 Single Inheritance
#2 Multiple Inheritance
#3 Multilevel Inheritance
#4 Hierarchical Inheritance
#5 Hybrid Inheritance

#ex

# class Car:
#     color = "black"
#     @staticmethod
#     def start():
#         print("car started..")

#     @staticmethod
#     def stop():
#         print("car stopped..")    

# class ToyotaCar(Car):
#     def __init__(self, name):
#         self.name = name


# car1 = ToyotaCar("fortuner")
# car2 = ToyotaCar("innova")

# print(car1.start())
# print(car2.color)

#Multiple Inheritance: When a class is derived from more than one base class, it is called multiple inheritance.

#ex:

# class A:
#     varA = "Welcome to class A"

# class B:
#     varB = "Welcome to class B"

# class C(A, B):
#     varC = "Welcome to class C"

# c1 = C()

# print(c1.varA)
# print(c1.varB)
# print(c1.varC)

#Super method: super() method is used to access methods of the parent class.

# class Car:
#     def __init__(self, type):
#         self.type = type

#     @staticmethod
#     def start():
#         print("car started..")

#     @staticmethod
#     def stop():
#         print("car stopped..")    

# class ToyotaCar(Car):
#     def __init__(self, name, type):
#         super().__init__(type)
#         self.name = name
#         super().start()

# car1 = ToyotaCar("prius", "electric")
# print(car1.type)

#class method: A class method is bound to the class & receives the class as an implicit first argument.
#note: static method can't access or modify class state & generally for utility.

#method=1

# class Person:
#     name = "anonymous"

    # def changeName(self, name):
    #     Person.name = name #(this will change the class attribute)(self.__class__.name = vaibahv) can also be used to change the class attribute
        #self.name = name (#this will change the instance attribute)

#method=2
#     @classmethod
#     def changeName(cls, name):
#         cls.name = name

# p1 = Person()
# p1.changeName("vaibhav")
# print(p1.name)
# print(Person.name)


#static method : this method in don't have access to the instance or class attributes. It is used to create utility functions.
#class method (cls):this method have access to the class attributes and can modify them. It is used to create factory methods.
#instance method (self): this method have access to the instance attributes and can modify them. It is used to create methods that operate on the instance data. 

#property decorator: we use @property decorater on any method in the class to use the method as a property.

# class Student:
#     def __init__(self, phy, chem, math):
#         self.phy = phy
#         self.chem = chem
#         self.math = math
#     #     self.percentage = str((self.phy + self.chem + self.math) / 3) + "%" #method=1

#     # def calcPercentage(self):
#     #     self.percentage = str((self.phy + self.chem + self.math) / 3) + "%"

#     @property  #method=2 this will allow us to access the method as a property without calling it as a method.
#     def percentage(self):
#         return str((self.phy + self.chem + self.math) / 3) + "%"
    
# stu1 = Student(90, 97, 99)
# print(stu1.percentage)        

# stu1.phy = 95
# # print(stu1.phy)
# # stu1.calcPercentage()
# print(stu1.percentage)        

#polymorphism: operator overloading
# when the same operator is allowed to have different meaning according to the context.

# + :

# print(1 + 2) #addition
# print(type(1))
# print("Vaibhav" + "Chauhan")#concatenate
# print(type("Vaibhav"))
# print([1, 2, 3] + [4, 5, 6])#merge lists
# print(type([1, 2, 3]))

#ex:

# class Complex:
#     def __init__(self, real, img):
#         self.real = real
#         self.img = img

#     def showNumber(self):
#         print(self.real, "i +", self.img, "j")

#     def add(self , num2):
#         newreal = self.real + num2.real
#         newImg =  self.img + num2.img
#         return Complex(newreal, newImg)

# num1 = Complex(1, 3)
# num1.showNumber()

# num2 = Complex(4, 6)
# num2.showNumber()

# num3 = num1.add(num2)
# num3.showNumber()


#Qs 1 

# Define a Circle class to create a circle with radius r using the constructor. 
# Define an Area() method of the class which calculate the area of the circle.
# Define a pwrimeter() method of the class which allows you to calculate the primeter of the circle.


#Qs 2

# Define a Employee class with attributes role, department & salary. This class showDetails()method.
# Create an Engineer class that inherits properties from Employee &     attributes: name & age.