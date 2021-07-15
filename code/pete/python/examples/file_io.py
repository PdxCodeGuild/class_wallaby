with open('fire-and-ice.txt', 'r') as f:
	print(f)
	poem = f.read()
improved_poem = poem.upper()
	# print(poem.split('\n'))
	# poem_lines = f.readlines()
	# print(poem_lines)
	# for line in poem_lines:
	# 	print(line.strip('\n'))
# poem_lines = poem.split('\n')

# print(improved_poem)

with open('FIRE-AND-ICE.txt', 'w') as f:
	f.write(improved_poem)