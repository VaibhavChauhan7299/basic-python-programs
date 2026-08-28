##Reverse a String:

# s = "Python"
# print(s[::-1])

## #List Comprehension:

# nums = [1, 2, 3, 4, 5]
# square = [x**2 for x in nums]
# print(square)

##Check  for a palinrome:

# def is_palindrome(words):
#     return words == words[::-1]
# print(is_palindrome("11122"))

##check with simple palindrome:

# def is_palindrome(s):
#     s = ''.join(c.lower()for c in s if c.isalnum()) #Convert to lowercase and remove non-aphanumeric characters(optional)
#     return s == s[::-1] # s[::-1] reverses the string 

# print(is_palindrome("radar"))
# print(is_palindrome("hello"))
# print(is_palindrome("A man, a plan, a canal: Panama")) 
# print(is_palindrome("12321"))

##Without using slicing (using two pointers):

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

## I have create a program to check if a number is prime or not:

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

## create a program to addition of multiple numbers using *args:
# *args allows you to pass a variable number of arguments to a function. Here's a simple program that demonstrates how to use *args to add multiple numbers:

# def add_numbers(*args):
#     return sum(args)

# # Example usage:

# result = add_numbers(*range(1, 101))
# print("The sum is:", result)

## write a program to merge 2 list without using the + operator:

# list1 = [1, 2, 3, 4, 5]
# list2 = [6, 7, 8, 9, 10]

# for i in list2:
#     list1.append(i)

# print("Merged list:", list1)    


## Zip

## Hostel data

# name = ['Ankur', 'Vaibhav', 'Rohit', 'Saurabh']

# bedroom = [101, 102, 103, 104]

# fee_status = ['Paid', 'Unpaid', 'Paid', 'Unpaid']

# all_data = list(zip(name , bedroom, fee_status))

# print(all_data)


## write a program to find the factorial of a number using recursion:

# def factorial(n):
#     if n == 0 or n == 1:
#         return 1
#     else:
#         return n * factorial(n - 1)

# print(factorial(5))  # Output: 120
# print(factorial(0))  # Output: 1
# print(factorial(1))  # Output: 1

## forloop method:

# n = int(input("Enter a number: "))

# factorial = 1

# for i in range(1, n + 1):
#     factorial *= i

# print("Factorial =", factorial)

## question: SWAP the key value pair for max and min values Eg if the dict is like this{'a': 1, 'b': 2, 'c': 3, 'd': 4} then the output should be like this {'a': 4, 'b': 2, 'c': 3, 'd': 1}

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

## Write a program to find the second largest number in a list:

# numbers = [10, 5, 8, 20, 15]

# numbers.sort(reverse=True)

# second_largest = numbers[1]

# print("The second largest number is:", second_largest)

##write a program to merge two dictionaries without using inbuilt function:

# dict1 = {
#     "name": "Vaibhav",
#     "age": 22
# }

# dict2 = {
#     "city": "Mumbai",
#     "country": "India"
# }

# merged_dict = {}

# for key in dict1:
#     merged_dict[key] = dict1[key]

# for key in dict2:
#     merged_dict[key] = dict2[key]

# print(merged_dict)

## write a program to find the common elements in two lists:

# list1 = [1, 2, 3, 4, 5]
# list2 = [4, 5, 6, 7, 8]

# common_elements = []

# for i in list1:
#     if i in list2:
#         common_elements.append(i)

# print("Common elements:", common_elements)

## how index giving for list:

# list = [10, 20, 30, 40, 50]

# for index, value in enumerate(list):

#  print(index, value)

## Write a program to find the sum of all even numbers in a list:

# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# even_sum = sum(num for num in numbers if num % 2 == 0)

# print("The sum of all even numbers is:", even_sum)

## write a program to find the largest number in a list:

# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# largest_number = max(numbers)

# print("The largest number in the list is:", largest_number)

##interview question: Write a program to find the missing number in a list of consecutive numbers:

# def find_missing_number(numbers):
#     n = len(numbers) + 1  # Total number of elements including the missing one

#     expected_sum = n * (n + 1) // 2  # Sum of first n natural numbers

#     actual_sum = sum(numbers)  # Sum of the given list

#     missing_number = expected_sum - actual_sum  # The missing number is the difference

#     return missing_number

# Example usage:

# numbers = [1, 2, 3, 4, 6, 7, 8, 9, 10]  # Missing number is 5

# missing_number = find_missing_number(numbers)

# print("The missing number is:", missing_number)

#perform union and intersection on 2 given list:

# list1 = [1, 2, 3, 4, 5]
# list2 = [4, 5, 6, 7, 8]

# union = []
# intersection = []

# for x in list1:
#     if x not in union:
#         union.append(x)

# for x in list2:
#     if x not in union:
#         union.append(x)        

#     print(union)

# for x in list1:
#     if x in list2 and x not in intersection:
#         intersection.append(x)

# print(intersection)

##write program remove duplicate characters:

# def remove_duplicates(s):
#     result = ""
#     for ch in s :
#         if ch not in result:
#             result += ch
#     return result

# print(remove_duplicates("programming"))  # Output: "progamin"

##write a proram from a list of numbers, move zero to the end of the list.

# list = [0, 1, 2, 0, 3, 4, 0, 5]

# for item in list:
#     if item == 0:

#         list.remove(item)
#         list.append(item)

# print(list)        

#reverse string:

# str = "Vaibhav Chauhan"
# str1 = ""

# for i in str:
#     str1 = i + str1

# print(str1)

##write a function to compress a string using Run-Length Encoding (RLE). The function should take a string as input and return the compressed version of the string. For example, the input "aaabbbcc" should return "a3b3c2".

# text = "aaabbbcc"

# def compress(text):
#     result = ""
#     count = 1

#     for i in range(len(text) - 1):
#         if text[i] == text[i + 1]:
#             count += 1
#         else:
#             result += text[i] + str(count)
#             count = 1

                
#     result = result + text[-1] + str(count)  # Add the last character and its count

#     return result

# print(compress(text))


##write a program to find the longest common prefix among a list of strings. If there is no common prefix, return an empty string.

# def longest_common_prefix(strings):
#     if not strings:
#         return ""

#     prefix = strings[0]

#     for string in strings[1:]:
#         while not string.startswith(prefix):
#             prefix = prefix[:-1]
#             if not prefix:
#                 return ""

#     return prefix

# # Example usage:
# strings = ["flower", "flow", "flight"]
# result = longest_common_prefix(strings)
# print("The longest common prefix is:", result)  # Output: "fl"


##write a program to find the first non-repeating character in a string. If all characters are repeating, return None.

# def first_non_repeating_character(s):
#     char_count = {}
    
#     # Count occurrences of each character
#     for char in s:
#         char_count[char] = char_count.get(char, 0) + 1

#     # Find the first non-repeating character
#     for char in s:
#         if char_count[char] == 1:
#             return char

#     return None

# Example usage:
# text = "abccba"
# result = first_non_repeating_character(text)
# print("The first non-repeating character is:", result)  # Output: None

##count how many numbers fall into each range(bin)of the given size and store the result in a directory. :

# numbers = [2, 5, 7, 8, 10, 12, 15, 18, 20, 22, 25]

# bin_size = int(input("Enter the bin size: "))

# histogram = {}

# for num in numbers:
#     bin_start = (num // bin_size) * bin_size
#     bin_end = bin_start + bin_size - 1
#     bin_range = str(bin_start) + "-" + str(bin_end)

#     if bin_range in histogram:
#         histogram[bin_range] = histogram[bin_range] + 1
#     else:
#         histogram[bin_range] = 1

# print("Histogram:", histogram)        

##write a program ton Transpose a matrix.

# matrix = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]

# result = []

# for i in range(len(matrix[0])):
#     row = []

#     for j in range(len(matrix)):
#         row.append(matrix[j][i])

#     result.append(row)

# print(result)  # Output: [[1, 4, 7], [2, 5, 8], [3, 6, 9]]

##Check whether two dictionaries are equal without using == operator:

# dict1 = {'a': 1, 'b': 2, 'c': 3}
# dict2 = {'c': 3, 'b': 2, 'a': 1}

# def check_equal(dict1, dict2):
#     if len(dict1) != len(dict2):
#         return False

#     for key in dict1:
#         if key not in dict2:
#             return False

#         if dict1[key] != dict2[key]:
#             return False

#     return True

# if check_equal(dict1, dict2) is True:
#     print("Both are equal")
# else:
#     print("Both are not equal")    

##write a program to repeated Alphabet Triangle.

# rows = int(input("Enter the number of rows: "))

# for i in range(1, rows + 1):
#     for j in range(i):
#         print(chr(64 + i), end=" ")
#     print()


##find all duplicate elements in a list along with their frequncies.:

# lst = [1, 2, 3, 4, 5, 2, 3, 4, 4, 5]

# feq = {}

# for i in lst:
#     if i in feq:
#         feq[i] = feq[i] + 1
#     else:
#         feq[i] = 1

#  for key in feq:
#     if feq[key] > 1:
#      print(key, ":", feq[key])

##write a function to rotate a square matrix 90 degrees clockwise.

# mat = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]

# def rotate_matrix(mat):

#     for i in range(len(mat)):
#         for j in range(i + 1, len(mat)):
#             mat[i][j], mat[j][i] = mat[j][i], mat[i][j]

#     for row in mat:
#         row.reverse()

#         return mat

# print(rotate_matrix(mat))  # Output: [[7, 4, 1], [8, 5, 2], [9, 6, 3]]
""""
##intervie question:
                    if[]:
                        print("yes")
                    else:
                        print("no")
                        """
## ans is no beacause empty list is considered as false in python.

##python program to find the sum of all prime numbers in a given range:

# def is_prime(n):
#     if n <= 1:
#         return False
#     for i in range(2, int(n**0.5) + 1):
#         if n % i == 0:
#             return False
#     return True

# def sum_of_primes(start, end):
#     total = 0
#     for n in range(start, end + 1):
#         if is_prime(n):
#             total += n
#     return total

# print(sum_of_primes(1, 10))  # Output: 17 (2 + 3 + 5 + 7)

##python program to display the Fibonacci sequence up to a given number of terms:

# def fibonacci_sequence(n):
#     sequence = []
#     a, b = 0, 1
#     for _ in range(n):
#         sequence.append(a)
#         a, b = b, a + b
#     return sequence

# print(fibonacci_sequence(10))  # Output: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]

##python program to check if a given number is an Armstrong number:

# def is_armstrong_number(num):
#     num_str = str(num)
#     num_len = len(num_str)
#     total = sum(int(digit) ** num_len for digit in num_str)
#     return total == num

# print(is_armstrong_number(153))  # Output: True
# print(is_armstrong_number(123))  # Output: False

##python program to find the GCD (Greatest Common Divisor) of two numbers using the Euclidean algorithm:

# def gcd(a, b):
#     while b:
#         a, b = b, a % b
#     return a

# print(gcd(48, 18))  # Output: 6

##python program to find the LCM (Least Common Multiple) of two numbers:

# def lcm(a, b):
#     return abs(a * b) // gcd(a, b)

# print(lcm(4, 5))  # Output: 20

##python program to check if a given string is a valid palindrome, considering only alphanumeric characters and ignoring cases:

# def is_valid_palindrome(s):
#     s = ''.join(c.lower() for c in s if c.isalnum())
#     return s == s[::-1]

# print(is_valid_palindrome("A man, a plan, a canal: Panama"))  # Output: True
# print(is_valid_palindrome("race a car"))  # Output: False

##python program to display the Pascal's triangle up to a given number of rows:

# def pascal_triangle(n):
#     triangle = []
#     for i in range(n):
#         row = [1] * (i + 1)
#         for j in range(1, i):
#             row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]
#         triangle.append(row)
#     return triangle

# print(pascal_triangle(5))  # Output: [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]

##python program to display all prime numbers within an interval:

# lower = 100
# upper = 120

# print("Prime numbers between", lower, "and", upper, "are:")

# for num in range(lower, upper + 1):
    #all prime numbers are greater than 1

    # if num > 1:
    #     for i in range(2, num):
    #         if (num % i) == 0:
    #             break
    #     else:
    #         print(num)

##write a python program to dungeon game where the player has to navigate through a maze and collect treasures while avoiding traps. The player can move in four directions (up, down, left, right) and the game ends when the player reaches the exit or falls into a trap.

# def dungeon_game():
#     maze = [
#         ['S', '.', '.', 'T', '.'],
#         ['.', 'T', '.', '.', '.'],
#         ['.', '.', 'T', 'T', '.'],
#         ['.', '.', '.', '.', 'E']
#     ]
    
#     player_pos = [0, 0]  # Starting position (row, col)
#     treasures_collected = 0
    
#     while True:
#         print_maze(maze, player_pos)
#         move = input("Enter your move (up, down, left, right): ").strip().lower()
        
#         if move == "up":
#             new_pos = [player_pos[0] - 1, player_pos[1]]
#         elif move == "down":
#             new_pos = [player_pos[0] + 1, player_pos[1]]
#         elif move == "left":
#             new_pos = [player_pos[0], player_pos[1] - 1]
#         elif move == "right":
#             new_pos = [player_pos[0], player_pos[1] + 1]
#         else:
#             print("Invalid move. Try again.")
#             continue
        
#         if is_valid_move(maze, new_pos):
#             player_pos = new_pos
#             if maze[player_pos[0]][player_pos[1]] == 'T':
#                 treasures_collected += 1
#                 maze[player_pos[0]][player_pos[1]] = '.'  # Collect treasure
#                 print(f"You collected a treasure! Total treasures: {treasures_collected}")
#             elif maze[player_pos[0]][player_pos[1]] == 'E':
#                 print(f"You reached the exit! Total treasures collected: {treasures_collected}")
#                 break
#             elif maze[player_pos[0]][player_pos[1]] == 'T':
#                 print("You fell into a trap! Game over.")
#                 break
#         else:
#             print("You can't move there. Try again.")

## Practice: Check even or odd

# number = 10

# if number % 2 == 0:
#     print("Even number")
# else:
#     print("Odd number")

##write a hard program to find the longest palindromic substring in a given string. A palindromic substring is a sequence of characters that reads the same backward as forward.

# def longest_palindromic_substring(s):
#     if len(s) < 1:
#         return ""

#     start, end = 0, 0

#     for i in range(len(s)):
#         len1 = expand_around_center(s, i, i)      # Odd length palindromes
#         len2 = expand_around_center(s, i, i + 1)  # Even length palindromes
#         max_len = max(len1, len2)

#         if max_len > (end - start):
#             start = i - (max_len - 1) // 2
#             end = i + max_len // 2

#     return s[start:end + 1]

# def expand_around_center(s, left, right):
#     while left >= 0 and right < len(s) and s[left] == s[right]:
#         left -= 1
#         right += 1
#     return right - left - 1
