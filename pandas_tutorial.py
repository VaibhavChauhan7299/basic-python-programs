import pandas as pd

#series: 

# x = [1, 2, 3, 4, 5] #list 

# s = pd.Series(x, index = ['a', 'b', 'c', 'd', 'e'], dtype = "float", name = "My First Series")

# print(s)

# print(type(s))

# print(s['e'])#output: 5

#dictionary

# dict = {"name":["python", "c", "c++", "java"], "por":[12, 13, 14, 15], "rank": [1, 4, 3, 2]}
# var1 = pd.Series(dict)

# print(var1)

#####

# s = pd.Series(12, index = [1,2,3,4,5,6,7,8,9,10])
# print(s)
# print(type(s))

# s1 = pd.Series(12, index = [1,2,3,4,5,6,7,8,9,10])
# s2 = pd.Series(12, index = [1,2,3,4,5])

# print(s1+s2) #output: 1    24.0
# print(s1-s2) #output: 1     0.0
# print(s1*s2) #output: 1    144.0
# print(s1/s2) #output: 1    1.0
# print(s1)
# print(s2)

#DataFrame:
# l = [1,2,3,4,5,6,7,8,9,10] #list

# var = pd.DataFrame(l)
# print(type(var))

#dictionary
# d = {"a":[1,2,3,4,5], "b":[6,7,8,9,10], "c":[11,12,13,14,15]}

# var1 = pd.DataFrame(d, columns = ["a", "b"], index = ["row1", "row2", "row3", "row4", "row5"])
# var1 = pd.DataFrame(d)
# print(var1["a"][3])

#list of list

list_1 = [[1,2,3,4,5], [6,7,8,9,10], [11,12,13,14,15]]

var2 = pd.DataFrame(list_1)
print(var2)
print(type(var2))