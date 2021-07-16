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
 
called_on_students = []

while True:
	student = random.choice(students)

	if student in called_on_students:
		continue

	called_on_students.append(student)
	print(student)
	
	if input() or len(students) == len(called_on_students):
		break 	