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

print(''.join(output))
new = []
list = (3, 2, 1)
for i in range(len(list)):
   i = i + 13 
#    new.append(list[i])
# print(new)'''

# board = [

#      ["1", "2-", "3-"],
#      ["-", "-", "-"],
#      ["-", "-", "-"]
#      ]
# class Game:
#    def _repr_(self, board):
#       for row in board: # goes through rows 
#          for j in row:  # goes through each string in each ro
#             returnprint(j, end=" ")

# game = Game()

# game._repr_(print(board))
# from string import punctuation
# def check_palindrome(string):
#    string = string.lower()
#    string = string.replace(' ','')
#    string = string.replace('!','')
#    string = string.replace("'",'')

#    rev_string = string[::-1]
#    if string == rev_string:
#       return True
#    return False, string

# print(check_palindrome("Go Hang a Salami! I'm a Lasagna Hog!"))

# x = 'dormitory'
# lst = []
# for i in x:
#    lst.append(i)
# print(lst)
# lst_1 = lst.sort()
# x = list('dormitory')
# y = list("abcde")
# if x == y:
#    print("yes")
# else:
#    print('no')

# string = "abc"
# print([i for i, x in enumerate(string)])




import requests
from datetime import datetime


payload = {'dt_text':'2021-07-27 21:00:00'}
headers_dict = {'dt_txt':'something'}
r = requests.get(f'http://api.openweathermap.org/data/2.5/forecast?q=portland&units=imperial&appid=884cfd64f3a52a3354c76c381207cf1e', params=payload)
r = r.json()


i = 0
while True:   
   for the in r:
      
      dt = int(r['list'][i]['dt'])
      
      
      date = datetime.utcfromtimestamp(dt).strftime('%Y-%m-%d %I:%M:%p')
      date = date.split(' ')
      temp = r['list'][i]['main']['temp']
      feels =r['list'][i]['main']['feels_like']
      max = r['list'][i]['main']['temp_max']
      min= r['list'][i]['main']['temp_min']
      print(f'For the date of {date[0]} at {date[1]} the expected temp will be {temp}F but will feel like {feels}F. The max temp will be {max}F and the min will be {min}F.')
      i += 1
   if i >= 40:
      break
      