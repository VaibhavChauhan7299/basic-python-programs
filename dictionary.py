#Dictionary
#Dictionaries are used to store data values in key:value pairs they are unordered, mutable(changeable)& don't allow duplicate keys

# info = {
#     "key" : "value",
#     "name" : "vaibhav",
#     "learning" : "coding",
#     "age" : 35,
#     "is_adult" : True,
#     "marks" : 94.4,
#     "name" : "VAIBHAVCHAUHAN",
#     "subjects" : ["python", "c", "Java"],
#     "topics" : ("dict", "set"),
# }

# print(info)
# print(type(info))
# print(info["subjects"])

# info["name"] = "yashvi" #overwrite
# info["surname"] = "sidapara"
# print(info)

#nested dictionary

student = {
    "name" : "rahul kumar",
    "subjects" : {
        "phy" : 97,
        "chem" : 98,
        "math" : 95
    }
}
#print(student["subjects"])

#dictionary methods

# myDict.keys()#return all keys
# myDict.values()#returns all values
# myDict.items()#return all(key, val)pairs as tuples
# myDict.get("key"")#returns the key according to value
# myDict.update(newDict)#inserts the specified items to the dictionary           

#print(len(list(student.keys())))
#print(list(student.values()))

#pairs=list(student.items())
#print(pairs[1])

# print(student["name"])
# print(student.get("name"))

# student.update({"city" : "delhi"})
# print(student)

# new_dict = {"city" : "delhi"}
# student.update(new_dict)
# print(student)