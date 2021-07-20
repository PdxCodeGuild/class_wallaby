english_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

user_str = input("Type a secret message for encryption: ")

user_str_lst = list(user_str)
# print(user_str_lst)

# compare letters in secret message list to rot_13_list
# take letters from secret message list and compare to english_list
# replace each letter with letter from rot13_list at that index 



def encryption(message):
    output_lst = []
    for i in range(len(message)): 
        #if i in message:
        x = english_list[(i + 13) % 26]
        output_lst.append(x)
        # print(message[i], i)
    return output_lst

print(encryption(user_str_lst))

# test: 'help me' = 'uryc zr'

