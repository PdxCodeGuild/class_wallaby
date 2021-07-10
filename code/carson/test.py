students = ('julio' ,'megan' , 'carson')
for student in students:
    print(student.capitalize())

from random import choice 
from colorama import init, Fore

init()

colors = [
Fore.BLACK,
Fore.RED,
Fore.GREEN,
Fore.YELLOW,
Fore.BLUE
    
]
def random_color():
    return choice (colors)

print(random_color())