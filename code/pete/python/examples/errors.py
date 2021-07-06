# print(1)
# print(2)
# print(3)
# print(4)

# print(1 + '1') # TypeErrors will crash your code when that line runs
# if: # IndentationErrors and SyntaxErrors will stop your program from running in the first place

# print(wallaby) #N NameError: variable is not defined

# abc = 'abcdefg'
# abc.append('hijklmnop') # AttributeError method or property does not belong to that type of object

# TypeErrors occur when you're trying to do something with an object that can't be done
# not_a_list = 123
# not_a_list = [1,2,3]
# not_a_list[0] = 2 #
# for num in not_a_list:
#     print(num)

# raise ValueError("This code is not very valuable") # raise your own error

try:
    x = 1 + '1'
    print(x)
except:
    print("An error occured")