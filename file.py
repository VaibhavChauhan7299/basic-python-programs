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