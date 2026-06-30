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