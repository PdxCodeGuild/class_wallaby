from random import random
from time import sleep

class Cat:
	# __init__ is a special method that runs with an object of the class is instantiated
	# self is always going to be the first parameter to a an object's methods
	def __init__(self, name, color, lives=9):
		self.name = name
		self.color = color
		self.lives = lives
	
	def meow(self):
		print('meow')
	
	def introduce(self):
		self.meow()
		print(f"I'm {self.name} the cat.  My fur is {self.color} and I have {self.lives} lives.")
		self.meow()

	def jump(self):
		print(f'{self.name} jumps...')
		sleep(1)
		if random() < .25:
			print(f'Ouch.  {self.name} fell.')
			self.lives -= 1
		else:
			print('Nice jump.')
		sleep(1)
		print(f'{self.name} has {self.lives} lives remaining.')
	
	def __str__(self):
		return self.name


garfield = Cat('Garfield', 'orange')
print(garfield)
# print(garfield.name)
# print(garfield.color)
# print(garfield.lives)

# garfield.meow()
garfield.introduce()

for _ in range(8):
	garfield.jump()

print()

# felix = Cat('Felix', 'black')
# print(felix)
# print(felix.name)
# print(felix.color)
# print(felix.lives)

# felix.meow()
# felix.introduce()

# string method .upper()
# text = 'abc'
# text.upper()