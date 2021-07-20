import string

alphabet = string.ascii_lowercase

# english_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

user_str = input("Type a secret message for encryption: ")

user_str_lst = list(user_str)
# print(user_str_lst)

def encryption(message):
    output_lst = []
    for i in range(len(message)):
        letter = message[i] 
        new_index = alphabet.index(letter) + 13
        print(alphabet[new_index % 26])
        # output = ''.join(alphabet[new_index % 26])
    # return output

# deal with spaces
        
        
#         print(english_list.index(letter))
#         if user_str_lst != english_list:
#             letter = english_list[(i + 13) % 26]
#             output_lst.append(letter)
#             # print(message[i], i)
#         output = ''.join(output_lst)
#     return output

print(encryption(user_str_lst))

# test: 'help me' = 'uryc zr'

