#file I/O in python

#python can be used to perform operations on a file.(read & write data)

#types of files:
#1. Text files (.txt, .csv, .html, .xml, .json, .py, .java, .c, .cpp, etc.)
#2. Binary files (.bin, .dat, .exe, .jpg, .png, .mp3, .mp4, etc.)

#Open, Read & Close File

#we have to open a file before reading or writing.

#f = open("file_name", "mode")

# f = open("lists.py" , "r") #opens the file in read mode
# data = f.read(5) #reads first 5 characters from the file
# print(data)
# print(type(data))
# f.close() #closes the file

#modes:
#charcter                       meaning
# "r" - open for reading (default)
# "w" - open for writing, truncating the file first
# "x" - create a new file and open it for writing
# "a" - open for writing, appending to the end of the file if exists
# "b" - binary mode
# "t" - text mode (default)
# "+" - open a file for updating (reading and writing)

#reading a file:

# data = f.read() #reads the entire file

# line = f.readline() #reads one line from the file


# f = open("loops.py", "r")

# line1 = f.readline()
# print(line1)

# line2 = f.readline()
# print(line2)

# f.close()

#writing to a file:

# f = open("sample.txt", "w") #opens the file in write mode

# f = open("demo.txt", "w") #opens the file in write mode
# f.write("I Love Python Programming")

# f = open("demo.txt", "a")
# f.write("\nbut I am learning java too.")
# f.close()

# f = open("demo.txt", "r+") #opens the file in read and write mode
# f.read("\nThis is new line added.")

# f = open("demo.txt", "w+")
# f.write("This is new line added.")
# print(f.read())
# f.write("This is another new line.")
# f.close()

#simply clarify and syntax of modes:

# r+  read+ overwrite (point to the beginning) and does not truncate
# w+  write+ truncate (at the beginning)
# a+  append+ (point to the end) and does not truncate

# with syntax:

# with open("demo.txt", "r") as f:
#     data = f.read()
#     print(data)

# with open("demo.txt", "w") as f:    
#     data = f.write("NEW DATA")
#     print(data)

#deleting a file:
# using the os module
# Module (like a code library) is a file written by another programmer that generally has a funtions we can use.

# import os
# os.remove("demo.txt")

#create a new file "practice.txt" using python. Add the following data in it:

# Hi everyone
# we are learning File I/O 
# using python.
# i like programming in python.

# with open("practice.txt", "w")as f:
#     f.write("Hi everyone\nwe are learning file I/O\nusing python.\ni like programming in python.")

#write a functions that replaced occurrences of "python" with "java" in above file

# with open("practice.txt", "r") as f:
#     data = f.read()

# new_data = data.replace("python", "java")    
# print(new_data)    

# with open("practice.txt", "w") as f:            #overwrite
#     f.write(new_data)

#Serach if the word "learning" exists in the file or not.

# def check_for_word():
#     word = "learning"
#     with open("practice.txt", "r") as f:
#         data = f.read()
#     if(data.find(word) != -1):  #if(word in data)
#         print("found")
#     else:
#          print("not found")   

# check_for_word()

#write a function to find in which line of the file does the word "learning" occur first.
# print -1 if word not found.

# def check_for_line():
#     word = "learning"
#     data = True
#     line_no = 1
#     with open("practice.txt", "r") as f:
#         while data:
#             data = f.readline()
#             if(word in data):
#                 print(line_no)
#                 return
#             line_no += 1
#     return -1

# print(check_for_line())

# From a file containing numbers separated by comma, print the count of even numbers.

#compelete scratch type:basic

# with open("practice.txt", "r") as f:
#     data = f.read()
#     print(data)

#     num = ""
#     for i in range(len(data)):
#         if(data[i] == ","):
#             print(int(num))
#             num = ""
#         else:
#             num += data[i]    

# second way for this
count = 0
with open("practice.txt", "r") as f:
    data = f.read()

    nums = data.split(",")
    for val in nums:
        if(int(val) % 2 == 0):
            count += 1

print(count)            