'''given_number = int(input('Enter a number: '))
tens_digit = given_number//10
ones_digit = given_number%10
print(tens_digit, ones_digit) 

too_many_mangos = ['apples', 'mangos', 'bananas', 'mangos', 'blueberries', 
'mangos', 'oranges', 'mangos', 'mangos']

# while 'mangos' in too_many_mangos:
   # too_many_mangos.remove('mangos')
# print(too_many_mangos) 

Dict_1 = {'1': 'one hundred', '2': 'two hundred', '3': 'three hundred', '4': 'four hundred', '5': 'five hundred', '6': 'six hundred', '7': 'seven hundred', 
'8': 'eight hundred', '9': 'nine hundred'}

print(Dict_1.get('1')) 

def cap(message):
   x = message.upper()
   return x

y = cap('hello')
print(y)
user_input = input("enter stuffs to be encrypted: ")
english = 'a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u, v, w, x, y, z'
rot_13 = 'n, o, p, q, r, s, t, u, v, w, x, y, za, b, c, d, e, f, g, h, i, j, k, l, m'

dict_1 = dict(zip(english, rot_13)) #https://stackoverflow.com/questions/11918909/how-do-i-create-a-dictionary-from-two-parallel-strings

output = []
for i in user_input:
    x = dict_1.get(i)

 
    output.append(x) 

print(''.join(output))'''
new = []
list = (3, 2, 1)
for i in range(len(list)):
   i = i + 13 
   new.append(list[i])
print(new)