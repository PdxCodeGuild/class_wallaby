import random

students = [
    'megan',
    'olana',
    'patrick',
    'julio',
    'carson',
    'chris',
    'westley'
]

while True:
	print(random.choice(students))
	if input():
		break