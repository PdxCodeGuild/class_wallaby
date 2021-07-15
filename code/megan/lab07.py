# import ascii?
# from string import ascii_uppercase
# from string import ascii_lowercase

# access: a[i]
# .replace
#for char in text: 

# lists?
english_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
rot_13_list = ['n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm']

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

secret_message = input("Type a secret message for encryption: "

# secret_message_list[-1] = '!'

# convert list back to string
# encrypted_message = ''.join
# print(encrypted_message)

# help from https://www.geeksforgeeks.org/rot13-cipher/
def encryption(secret_message):
    encrypted_message = ''
    for letter in secret_message:
        # check for spaces
        if letter != ' ':
            index = (english_dict[letter]) % 26
            encrypted_message += rot13_dict[index]
        else:
            encrypted_message += ' '
    return encrypted_message

print(encryption(secret_message))

# error -- fix dictionaries!

'''    
    for i in range(len(secret_message)):
        # take character at index in english_list and replace it with character in rot13_list at that index 
        if     
    return encrypted_message
print(encryption())
    
    counter = 0
    counter += 1 % len(user_str)
    print(counter)
print(encryption())

counter = 0

while True:
	index = counter % len(secret_message)
	letter = ascii_uppercase[index]
	print(index, counter)
	print(
	counter += 1
'''


