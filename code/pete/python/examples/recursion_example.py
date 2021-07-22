def for_loop(list, i=0):
	if i >= len(list):
		return
	print(list[i])
	i += 1
	for_loop(list, i)

numbers = [1,2,3,4,5]
for_loop(numbers)