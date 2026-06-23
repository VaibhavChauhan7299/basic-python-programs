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

class Account:
    def __init__ (self, bal, acc):
        self.balance = bal
        self.account_no = acc

    def debit(self, amount):
        self.balance -= amount
        print("Rs. ", amount, "was debited")
        print("total balance =", self.get_balance())



    def credit(self, amount):
        self.balance += amount
        print("Rs. ", amount, "was credited")
        print("total balance =", self.get_balance())


    def get_balance(self):
        return self.balance        
    
acc1 = Account (10000, 12345) 
# print(acc1.balance)
# print(acc1.account_no)   
acc1.debit(5000)
acc1.credit(2000)
acc1.credit(55000)