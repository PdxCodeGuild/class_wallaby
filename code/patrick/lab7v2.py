
places_2 = int(input('place to move - 1 thru 26: '))
user_input = input("enter stuffs to be encrypted: ")
english = 'abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz'

rot_1 = ""
for i in user_input:
    letter_index = english.index(i)
    rot_1 += english[letter_index + places_2]
#     print(rot_1)
    
print(rot_1)


