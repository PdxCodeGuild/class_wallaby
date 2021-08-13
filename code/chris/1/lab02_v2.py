list_of_nums = []
totalSum = 0
continue_flag = True

while continue_flag == True:
  new_num = input('\nEnter a number or type \'done\': ')
  if new_num == 'done':
    continue_flag = False
    break
  else:
    list_of_nums.append(int(new_num))

if len(list_of_nums) > 0:
  for num in list_of_nums:
    totalSum += num

  num_of_nums = len(list_of_nums)
  avg = totalSum / num_of_nums

  print(avg)
else:
  print(0)



