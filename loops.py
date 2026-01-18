#loops
#loops are used to repeat instructions.
#types of loops:
#1. for loop
#2. while loop

#while Loops

# count = 1
# while count<=5:
#     print("Hello Vaibhav")
#     count = count + 1
# print(count)

# i = 1
# while i<=100000:
#     print("YASHVIVAIBHAV", i)
#     i = i + 1
# print(i)
#not: make sure to update the condition variable inside the loop to avoid infinite loop.

#print numbers from 1 to 5
# i = 1
# while i<=5:
#     print(i)
#     i = i + 1
# print("Done")

#print muliplication table of 35 using while loop

# i = 1
# while i<=10:
#     print(35,"x",i,"=",35*i)
#     i = i + 1

#print number from 5 to 1

# i = 5
# while i>=1:
#     print(i)
#     i = i - 1
# print("Done")

#print number from 1 to 100

# i = 1 
# while i<=100:
#     print(i)
#     i = i + 1

#print number 100 to 1

# i = 100
# while i>=1:
#     print(i)
#     i = i - 1

#print the multiplication table of a number n.

# i = 1
# n = int(input("Enter the number :"))
# while i<=10:
#     print(n, "x", i, "=", n*i)
#     i+=1

#print the elements of the following list using a loop:
    
# values = [1,4,9,16,25,36,49,64,81,100]
# index = 0
# while index<len(values):
#     print(values[index])
#     index += 1

#example

# heros = ["Ironman", "Thor", "Hulk", "Captain America", "Black Widow"]
# i = 0
# while i<len(heros):
#     print(heros[i])
#     i += 1

#search for a number x in this tuple using loop:

# nums = (10, 23, 45, 70, 11, 3, 99, 34, 67)

# x = 70

# i = 0
# while i<len(nums):
#     if(nums[i] == x):
#         print("Found at index", i)
#         break
#     else:
#         print("finding...")    
#     i += 1
# print("End of loop")

#Break: used to terminate the loop when encountered.
#Continue: terinates execution in the current iteration & continues execution of the loop with next iteration.

# i = 1
# while i<=10:
#     print(i)
#     if (i == 5):
#         break
#     i += 1

# i = 0
# while i<10:
#     if(i%2 != 0):
#         i += 1
#         continue #skip
#     print(i)
#     i += 1

#loop are used for sequential traversal. for traversing list, string, tuples etc..

# names = ["Vaibhav", "Yashu", "Anuj", "Ritik"]
# for name in names:
#      print(name)

# tuple1 = (1, 2, 3, 4, 5)
# for num in tuple1:
#     print(num)

#when we work on itretors so using while loop.
#when datatypes on travers so using for loop.

# str = "Hello Vaibhav"
# for char in str:
#     print(char)
# else:
#     print("End of string")    

#print the elements of the following list using for loop:
#[1,4,9,16,25,36,49,64,81,100]

# value = [1,4,9,16,25,36,49,64,81,100]

# for val in value:
#     print(val)


# nums = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)

# biradar = int(input("enter number to search:"))
# for i in nums:
#     if(i == biradar):
#         print("BIRADAR FOUND")
#         break
#     else:
#         print("THIS IS NOT MY BIRADAR")    
 
#search for a number x in this tuple using loop:
#(1, 4, 9, 16, 25, 36, 49, 64, 81, 100)

# nums = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 16, 64, 16)
# x = 16

# index = 0
# for num in nums:
#     if (num == x):
#         print("found at index", index)
#     index += 1

#range() function
#Range functions returns a sequence of numbers, starting from 0 by default, and increments by 1 (by default), and stops beforea specified number.

# seq = range(10)

# for i in seq:
#     print(i)


