# STRING 

#string is data type that stores a sequence of characters.

# str1 = "Hello, World!"
# str2 = 'Python is fun.'
# str3 = """This is a string"""

# str1 = "This is a string..\t with a tab space."
# print(str1)

# str1 = "hello"
# len1 =len(str1)
# print(len1)

# str2 = "helluu"
# len2 =len(str2)
# print(len2)

# final_str = str1+ " " + str2
# print(str1+str2)
# print(final_str)
# print(len(final_str))

#indexing in string

# str = "Vaibhav Chauhan"
# ch =str[0]
# print(ch)

#slicing in string

# str = "Vaibhav Chauhan"
# print(str[0:7])  # Vaibhav
# print(str[8:15]) # Chauhan
# print(str[:7])   # Vaibhav
# print(str[6:])   # v Chauhan
# print(str[:])    # Vaibhav Chauhan

#negative indexing in string

# str = "Vaibhav Chauhan"
# print(str[-1])    # n
# print(str[-7:])   # Chauhan
# print(str[:-7])   # Vaibhav
# print(str[-7:-1]) # Chauha
# print(str[-15:]) # Vaibhav Chauhan

#string functions

str = "i am studying from sltiet"
#print(str.endswith("ET")) # True
#print(str.capitalize()) # I am studying from sltiet
# str = str.capitalize()
# print(str)
# print(str.replace("i am","Vaibhav Chauhan is")) # Vaibhav Chauhan is studying from SLTIET
# print(str.find("t"))
# print(str.count("t"))
# print(str.upper()) # I AM STUDYING FROM SLTIET
# print(str.lower()) # i am studying from sltiet

#Write a program to user's first name & print its length.

# str = ("vaibhav chauhan")
# print("length of string is :",len(str))

# name = input("Enter your first name:")
# print("length of your first name is:", len(name))

#write a program to find occurrence of '@' in a string.

# str = "vaibhav@chauhan , yashvi@sidapara , megh@vyas"
# print(str.count("@"))