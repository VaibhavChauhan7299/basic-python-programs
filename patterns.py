#programs of patterns in python:
#method 1: Star pattern:
# print("**************")
# print("*************")
# print("************")
# print("***********")
# print("**********")
# print("*********")
# print("********")
# print("*******")
# print("******")
# print("*****")
# print("****")
# print("***")
# print("**")
# print("*")

#method 2:

# i = 10
# print('*' * i)
# i = 9
# print('*' * i)
# i = 8
# print('*' * i)
# i = 7
# print('*' * i)
# i = 6
# print('*' * i)
# i = 5
# print('*' * i)
# i = 4
# i = 3
# print('*' * i)
# i = 2
# print('*' * i)
# i = 1
# print('*' * i)

#method 3:

# for i in range(10, 0, -1):
#     print('*' * i)

#method 4: 
# n = 5
# for i in range(n):
#     print('*' * (i + 1))

#method 5: reverse star pattern:

# n = 10
# for i in range(n):
#     print('*' * (n - i))

#number pattern:

# n = 10
# for i in range(n):
#     for j in range(i + 1):
#         print(j + 1, end='')
#     print()
    
#heart pattern:

# for i in range(6):
#     for j in range(7):
#         if (i == 0 and j % 3 != 0) or \
#         (i == 1 and j % 3 == 0) or \
#         (i - j == 2) or \
#         (i + j == 8):
#             print("*", end="")
#         else:
#             print(" ", end="")
#     print()