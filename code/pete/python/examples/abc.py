from random import choice
from string import ascii_uppercase
from time import sleep

from colorama import init, Fore
print()
init()

colors = [
	Fore.BLACK,
	Fore.RED,
	Fore.GREEN,
	Fore.YELLOW,
	Fore.BLUE,
	Fore.MAGENTA,
	Fore.CYAN,
	Fore.WHITE,
]

def random_color():
	return choice(colors) # random.choice returns a random object from an iterable (list, string, or other list-like object)

# for _ in range(10):
# 	sleep(0.25)
# 	print(random_color(), ascii_uppercase)

# for letter in ascii_uppercase:
# 	sleep(0.25)
# 	print(random_color(), letter)

# while True:
# 	for letter in ascii_uppercase:
# 		sleep(0.25)
# 		print(random_color(), letter)
ascii_uppercase += '☂'
counter = 0
while True:
	sleep(0.25)
	index = counter % len(ascii_uppercase)
	letter = ascii_uppercase[index]
	print(index, counter)
	print(random_color(), letter)
	counter += 1
