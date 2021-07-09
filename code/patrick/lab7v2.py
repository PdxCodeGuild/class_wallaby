places_2 = int(input('place to move: '))
user_input = input("enter stuffs to be encrypted: ")
english = 'abcdefghijklmnopqrstuvwxyz'

rot_13 = english[places_2:]

dict_1 = dict(zip(english, rot_13)) #https://stackoverflow.com/questions/11918909/how-do-i-create-a-dictionary-from-two-parallel-strings

output = []
for i in user_input:
    x = dict_1.get(i)
    output.append(x) 

print(''.join(output))  


