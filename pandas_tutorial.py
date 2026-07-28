import pandas as pd

#series: 

# x = [1, 2, 3, 4, 5] #list 

# s = pd.Series(x, index = ['a', 'b', 'c', 'd', 'e'], dtype = "int", name = "My First Series")

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

# list_1 = [[1,2,3,4,5], [6,7,8,9,10], [11,12,13,14,15]]

# var2 = pd.DataFrame(list_1)
# print(var2)
# print(type(var2))

#2 series to dataframe

# sr ={"r":pd.Series([1,2,3,4,5]), "s":pd.Series([6,7,8,9,10])}

# var3 = pd.DataFrame(sr)
# print(var3)
# print(type(var3))

#Arithmetic operations:

# var = pd.DataFrame({"A":[1,2,3,4,5], "B":[6,7,8,9,10],})

# var["C"] = var["A"] + var["B"]
# var["D"] = var["A"] - var["B"]
# var["E"] = var["A"] * var["B"]
# var["F"] = var["A"] / var["B"]

# print(var)

#logical operations:

# var1 = pd.DataFrame({"A":[10,20,30,40,50], "B":[15,16,17,18,19,]})
# print(var1)

# var1["Python"] = var1["A"] <= 20
# var1["Python_1"] = var1["B"] >= 16
# print(var1)

#Insert:

# var = pd.DataFrame({"A":[1,2,3,4,5], "B":[6,7,8,9,10]})

# var.insert(1, "Python", var["A"] )

# var.insert(1, "Python_1", [11,12,13,14,15])#second method

# var["Python_12"] = var["A"][:3]#copy need data and insert a new column

# print(var)

#Delete:

# var = pd.DataFrame({"A":[1,2,3,4,5], "B":[6,7,8,9,10], "C":[11,12,13,14,15]})

# var1 = var.pop("B")

# print(var1)
# print(var)

# del var["A"] #second method

# print(var)


# write CSV 

# how to create CSV file:

dis = {"R":[1,2,3,4,5], "S":[6,7,8,9,10], "C":[11,12,13,14,15], "Y":[16,17,18,19,20], "V":[21,22,23,24,25]}

d = pd.DataFrame(dis)

print(d)

d.to_csv("5_MembersF.csv", index=False)

