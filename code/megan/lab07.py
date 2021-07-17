from string import ascii_lowercase

english_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
rot_13_list = ['n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm']

secret_message = input("Type a secret message for encryption: ")

# turn string into list 
secret_message_list = list(secret_message)
print(secret_message_list)

# slicing
# print(secret_message[::13])
'''
encrypted_message = ''

# take user input as a string
# take character at index in english_list and replace it with character in rot13_list at that index 

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
'''