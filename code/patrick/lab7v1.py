user_input = input("enter stuffs to be encrypted: ")
english = 'a b c d e f g h i j k l m n o p q r s t u v w x y z'
rot_13 = 'n o p q r s t u v w x y z a b c d e f g h i j k l m'

dict_1 = dict(zip(english, rot_13)) #https://stackoverflow.com/questions/11918909/how-do-i-create-a-dictionary-from-two-parallel-strings
print(dict_1)
output = []
for i in user_input:
    x = dict_1.get(i)

 
    output.append(x) 

print(''.join(output))  