#Reverse a String:

# s = "Python"
# print(s[::-1])

# #List Comprehension:

# nums = [1, 2, 3, 4, 5]
# square = [x**2 for x in nums]
# print(square)

#Check  for a palinrome:

# def is_palindrome(words):
#     return words == words[::-1]
# print(is_palindrome("11122"))

#check with simple palindrome:
# def is_palindrome(s):
#     s = ''.join(c.lower()for c in s if c.isalnum()) #Convert to lowercase and remove non-aphanumeric characters(optional)
#     return s == s[::-1] # s[::-1] reverses the string 

# print(is_palindrome("radar"))
# print(is_palindrome("hello"))
# print(is_palindrome("A man, a plan, a canal: Panama")) 
# print(is_palindrome("12321"))

#Without using slicing (using two pointers):

# def is_palindrome(s):
#     s = ''.join(c.lower()for c in s if c.isalnum())#Convert to lowercase and remove non-aphanumeric characters(optional)
#     left, right = 0, len(s) - 1 # Initialize two pointers
#     while left < right:
#         if s [left] != s[right]:
#             return False
#         left += 1
#         right -= 1
#     return True


# class Circle:
#     def __init__(self, radius):
#         self.radius = radius

#     def area(self):
#         return (22/7) * self.radius ** 2

#     def perimeter(self):
#         return 2 * (22/7) * self.radius

# c1 = Circle(21)
# print(c1.area())
# print(c1.perimeter())

# a = 50
# b = 20

# print("Before swapping: a =", a, "b =", b)
# a, b = b, a
# print("After swapping: a =", a, "b =", b)

#I have create a program to check if a number is prime or not:

# def is_prime(n):
#     if n <= 1:
#         return False
#     for i in range(2, int(n**0.5) + 1):
#         if n % i == 0:
#             return False
#     return True

# user_input = int(input("Enter a number: "))

# if is_prime(user_input):
#     print(f"{user_input} is a prime number.")
# else:
#     print(f"{user_input} is not a prime number.")

#create a program to addition of multiple numbers using *args:
#*args allows you to pass a variable number of arguments to a function. Here's a simple program that demonstrates how to use *args to add multiple numbers:

# def add_numbers(*args):
#     return sum(args)

# # Example usage:

# result = add_numbers(*range(1, 101))
# print("The sum is:", result)

# write a program to merge 2 list without using the + operator:

# list1 = [1, 2, 3, 4, 5]
# list2 = [6, 7, 8, 9, 10]

# for i in list2:
#     list1.append(i)

# print("Merged list:", list1)    


#Zip
#Hostel data

# name = ['Ankur', 'Vaibhav', 'Rohit', 'Saurabh']

# bedroom = [101, 102, 103, 104]

# fee_status = ['Paid', 'Unpaid', 'Paid', 'Unpaid']

# all_data = list(zip(name , bedroom, fee_status))

# print(all_data)


#write a program to find the factorial of a number using recursion:

# def factorial(n):
#     if n == 0 or n == 1:
#         return 1
#     else:
#         return n * factorial(n - 1)

# print(factorial(5))  # Output: 120
# print(factorial(0))  # Output: 1
# print(factorial(1))  # Output: 1

#forloop method:

# n = int(input("Enter a number: "))

# factorial = 1

# for i in range(1, n + 1):
#     factorial *= i

# print("Factorial =", factorial)

#question: SWAP the key value pair for max and min values Eg if the dict is like this{'a': 1, 'b': 2, 'c': 3, 'd': 4} then the output should be like this {'a': 4, 'b': 2, 'c': 3, 'd': 1}

# dic = {
#     "a": 1,
#     "b": 2,
#     "c": 3,
#     "d": 4
# }

# max_key = max(dic, key = dic.get) # type: ignore
# min_key = min(dic, key = dic.get) # type: ignore

# dic[max_key], dic[min_key] = dic[min_key], dic[max_key]

# print(dic)

#Write a program to find the second largest number in a list:

# numbers = [10, 5, 8, 20, 15]

# numbers.sort(reverse=True)

# second_largest = numbers[1]

# print("The second largest number is:", second_largest)

#