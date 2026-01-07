#lists
# a built in data type that stores set of values , it can store elements of different types(integer , float , string , etc..

# marks = [94.4, 87.5, 95, 55, 99]
# print(marks)
# print(type(marks))
# print(marks[0])
# print(marks[1])

# student = ["John", 21, "A+", True]
# print(student)
# student[0] = "Yashu"
# print(student)

#list slicing
#list_name [starting_index : ending_index] #ending idx is not included

# marks = [85, 55, 90, 78, 88, 92, 67, 79]
# print(marks[1:4])
# print(marks[2:5])
# print(marks[0:3])
# print(marks[-4:-1])

#list methods

list = [5, 1, 5, 15, 20, 25]

# list.append(30) #adds one element at the end
# print(list)
# print(list.sort())# sorts in ascending order
# print(list)
# list.sort(reverse=True) #sorts in descending order
# print(list)
# list.reverse() #reverses the list
# print(list)
# list.insert(2, 10) #insert element at index
# print(list)
#list.remove(5) #removes first occurrence of elemenet
#print(list)
# list.pop(2) #removes element at idx
# print(list)

#write a program to ask the user to enter names of their 3 favorite movies & them in a list.

# movies = []
# mov1 = input("enter 1st movie:")
# mov2 = input("enter 2nd movie:")
# mov3 = input("enter 3rd movie:")

# movies.append(mov1)
# movies.append(mov2)
# movies.append(mov3)

# print(movies)

# 2 write a program to check if a list contains a palideome of elemnts.(hint:use copy()method)

list1 = [1, 2, 1]
list2 = [1, 2, 3]
copy_list1 = list1.copy()
copy_list1.reverse()

if(copy_list1 == list1):
    print("palindrome")
else:
    print("NOT palindrome")
    

    