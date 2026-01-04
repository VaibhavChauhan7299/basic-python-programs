#conditional statements

#if-elif-else statement

# num = 11

# if(num > 2):
#     print(" greater than 2")
#     if(num < 10):
#         print("num is less than 10")

# age = 20

# if (age >= 18):
#     print("You are eligible to vote")  #indentation
# else:
#     print("You are not eligible to vote")

#note: Python uses indentation to define blocks of code. and python in conditional statements use in first of all if condition is mandatory. if or elif many times use this condition but else only one time use in conditional statements.

# marks = int(input("enter your marks :"))

# if (marks >= 90):
#     grade = "A"
# elif (marks >= 80 and marks < 90):
#     grade  = "B"
# elif (marks >= 70 and marks < 80):
#     grade = "C"
# else:
#     grade = "D"

# print("grade of student is ->", grade)

#nested if-else statement

# age = int(input("enter your age :"))

# if (age >= 18):
#     if (age >= 80):
#         print("cannot drive")
#     else:
#         print("can drive")
# else:
#     print("cannot drive")        

#write a program to check if a number entered by the user  is odd or even.

# num = int(input("enter your number :"))
# if (num % 2 == 0):
#     print("number is even")
# else:
#     print("number is odd")

#write a program to find greatest of 3 numbers entered by the user.

# num1 = int(input("enter first number :"))
# num2 = int(input("enter second number :"))
# num3 = int(input("enter third number :"))

# if (num1 >= num2) and (num1 >= num3):
#     print("first number is greatest :", num1)
# elif(num2 >=num1) and (num2 >= num3):
#     print("second number is greatest :", num2)
# else:
#     print("third number is greatest :", num3) 

#write a program it check if a number is a multiple of 7 is or not.

# num = int(input("enter your number :"))
# if (num % 7 == 0):
#     print("number is multiple of 7")
# else:
#     print("number is not multiple of 7") 