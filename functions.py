#functions
#Block of statements that perform a specific task.
#def function_name(parameters):

# def func_name(parameters1, parameters2):
#function body
    
# a = 5
# b = 10

# sum = a + b
# print("Sum =", sum)

# def calculate_sum(a, b):
#     sum = a + b
#     print(sum)
#     return sum

# calculate_sum(5, 10)

# calculate_sum(20, 30)

#function defination 

# def calc_sum(a, b): #parameters
#     return a + b

# sum1 = calc_sum(3035, 104) #function call: arguments
# print(sum1)


# def print_hello():
#     print("Hello Vaibhav")

# print_hello()
# print_hello()
# print_hello()
# print_hello()
# print_hello()

# def print_hello():
#     print("Hello")

# output = print_hello()
# print(output)   #prints None because the function does not return any value

# def greet(name):
#     print("Hello", name)
# greet("Vaibhav")
# greet("Alice")
# greet("Bob")

# def add(a, b):
#     return a + b
# result = add(5, 10)
# print("Addition =", result)

#average of 3 numbers
# def calculate_average(num1, num2, num3):
#     sum = num1 + num2 + num3
#     average = sum / 3
#     print(average)
#     return average

# calculate_average(98, 97, 99)

#there are 2 types of functions:
#1. Built-in functions
#2. User-defined functions

#Built-in functions
# print() , input() , type() , len() , int() , str() , float() , list() , set() , dict() , tuple() , etc.

#example:
# print("Vaibhav")#sep: #this is a built-in function that prints the output to the console.
# print("Chauhan")#end:

# print("Vaibhav", end="  ")
# print("Chauhan")

#default parameters
#Assiging default values to parameters , which is used when no argument is passed.

# def cal_prod(a=1, b=1): #parameters with default values
#     print(a * b)
#     return a * b

# cal_prod(5, 10) #passing arguments


#write a function to print the length of a list. (list is the parameter)

# def print_length(lst):
#     print(len(lst))
#     return len(lst)

# print_length([1, 2, 3, 4, 5, 6, 7, 8, 9])

#ex2:

# cities = ["Delhi", "Mumbai", "Bangalore", "Chennai", "Kolkata"]
# heros = ["Ironman", "Spiderman", "Hulk", "Thor", "Captain America"]

# def print_list(lst):
#     print(len(lst))

# print_list(cities)
# print_list(heros)


#write a function to print the elements of a list in a single line (list is the parameter).

# heros = ["Ironman", "Spiderman", "Hulk", "Thor", "Captain America"]

# def print_elements(lst):
#     for element in lst:
#         print(element, end=" ")
#     print()
        
# print_elements(heros)

#write a funciton to find the maximum number in a list. (list is the parameter)

# def find_max(lst):
#     max_num = lst[0]
#     for num in lst:
#         if num > max_num:
#             max_num = num
#     print("Maximum number is:", max_num)
#     return max_num        

# find_max([10, 25, 3, 99, 56, 78, 34])
# find_max([-10, -25, -3, -1, -56, -78, -34])
# find_max([0, 0, 0, 0, 0])

#write a function to find factorial of a n. (n is the parameter)

# def factorial(n=1):
#     fact = 1
#     for i in range(1, n +1):
#         fact *= i
#     print("Factorial of", n, "is:", fact)
#     return fact

# factorial(5)
# factorial(0)
# factorial(7)

# write a function to convert USD to INR.(usd_value is the parameter)

# def converter(usd_value):
#     inr_value = usd_value * 82.74
#     print(usd_value, "USD =", inr_value, "INR")

# converter(100)
# converter(250.5)
# converter(50)

#write a function to user input check number is even or odd . (n is the parameter)

# def check_even_odd(i):
#     if n % 2 == 0:
#         print(n, "is Even")
#     else:
#         print(n, "is Odd")
#     return

# n = int(input("Enter a number: "))
# check_even_odd(n)



#Recursion
#when a function calls itself repeatedly.

# def show(n):
#     if(n == 0): #base case
#         return
#     print(n)
#     show(n-1)
#     print(END)
# show(5)


# def factorial(n):
#     if(n == 0 or n == 1): #base case
#         return 1
#     return factorial(n-1) * n

# result = factorial(5)
# print("Factorial =", result)