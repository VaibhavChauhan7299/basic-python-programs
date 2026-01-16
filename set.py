#set
#set is the collection of the unorderd items.
#Each element in the set must be unique & immutable.

# collection = {1,2,2,3,4, "hello", "world"}

# print(collection)
# print(type(collection))
# print(len(collection))

#collection = set()
#print(collection)

#set Methods

# set.add(el)#adds an element
# set.remove(el)#removes the elem an
# set.clear()#emties the set
# set.pop()#removes a random value
#set.union(set2)#combines both set values & returns new
#set.intersection(set2)#combines common value & returns new

# collection = set()
# collection.add(1)
# collection.add(2)

# collection.remove(1)
# collection.clear()
# print(collection)

# collection = {"Hello", "Vaibhav", "World", "Python"}

# print(collection.pop())
# print(collection.pop())

# set1 = {1,2,3}
# set2 = {2,3,4}

# print(set1.union(set2))
# print(set1)
# print(set2)

# print(set1.intersection(set2))
# print(set1)
# print(set2)

#you are given a list of subjects for students. Assume one classroom is required for 1 subject. How many classrooms are needed by all students.

# subjects = {
#     "python", "java", "c++", "python", "java", "javascript",
#     "python", "c++","c"
# }

# print(len(subjects))

#Figure out a way to store 9 & 9.0 as separate values in the set.
#(You can take help of built-in data types)

#solutuion-1
values = {9, "9.0"}
print(values)

#solution-2

# values = {
#     ("float", 9.0),
#     ("int", 9)
# }
# print(values)