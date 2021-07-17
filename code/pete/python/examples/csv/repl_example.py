from random import *
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet']
while True:
	user_input = input("""
		Welcome to the RANDOMizer what randomness do you want???
		1: random float from 0 to 1
		2: random integer from 1 to 100
		3: random color
		or 'done' to quit
	""")
	if user_input == '1':
		print(random())
	elif user_input == '2':
		print(randint(1, 100))
	elif user_input == '3':
		print(choice(colors))
	elif user_input == 'done':
		break
	else:
		print('Please enter a valid input :)')
print('Thanks for using RANDOMizer.')