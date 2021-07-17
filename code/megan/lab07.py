# from string import ascii_lowercase?

english_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
rot_13_list = ['n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm']

# take user input as a string
user_str = input("Type a secret message for encryption: ")

# turn string into list 
user_str_lst = list(user_str)
print(user_str_lst)

# compare letters in secret message list to rot_13_list
# take letters from secret message list and compare to english_list
# replace each letter with letter from rot13_list at that index 

def encryption():
    output_lst = []
    for i in range(len(english_list) - 1):
    # for letter in secret_message_list:
        # check for spaces
        while i != ' ':
            output_lst = user_str_lst[(i + 13) % 26]
        else:
            output_lst += ' '
    return output_lst

print(encryption())

# slicing?
# print(secret_message[::13])

# enumerate?

'''
encrypted_message = ''


english_list[i]

for i, letter in enumerate(english_list):
    encrypted_message = english_list[(i + 13) % 26]

for i in range(len(english_list)):
    encrypted_message = ''
    encrypted_message = english_list[(i + 13) % 26]

for char in secret_message:
    print(char)
print(secret_message[0])

secret_message_list = list(secret_message)
print(secret_message_list)

for letter in secret_message_list:
    secret_message_list[13].replace

print(encrypted_message)

#for letter in string.ascii_lowercase:
#    print(ord(letter), chr(ord(letter)))
#test = 'hello world'
#print(test.replace('hello', 'goodbye'))
'''

# access: a[i] (lists + assignment; dictionaries)
# .replace (strings)
# for char in text: (strings)

# dictionaries?
english_dict = {
    0: 'a',
    1: 'b',
    2: 'c',
    3: 'd', 
    4: 'e', 
    5: 'f', 
    6: 'g', 
    7: 'h', 
    8: 'i', 
    9: 'j', 
    10: 'k', 
    11: 'l', 
    12: 'm', 
    13: 'n', 
    14: 'o', 
    15: 'p', 
    16: 'q', 
    17: 'r', 
    18: 's', 
    19: 't', 
    20: 'u', 
    21: 'v', 
    22: 'w', 
    23: 'x', 
    24: 'y', 
    25: 'z'
}

rot13_dict = {
    0: 'n',
    1: 'o',
    2: 'p',
    3: 'q', 
    4: 'r', 
    5: 's', 
    6: 't', 
    7: 'u', 
    8: 'v', 
    9: 'w', 
    10: 'x', 
    11: 'y', 
    12: 'z', 
    13: 'a', 
    14: 'b', 
    15: 'c', 
    16: 'd', 
    17: 'e', 
    18: 'f', 
    19: 'g', 
    20: 'h', 
    21: 'i', 
    22: 'j', 
    23: 'k', 
    24: 'l', 
    25: 'm'
}