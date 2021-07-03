list_of_nums = [5, 0, 8, 3, 4, 1, 6]
totalSum = 0
num_of_nums = len(list_of_nums)

for num in list_of_nums:
  totalSum += num

avg = totalSum / num_of_nums

print(avg)
