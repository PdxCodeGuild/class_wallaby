def linear_search(nums, value):
  counter = 0
  reader = nums[counter]
  while reader != value:
    if counter >= len(nums) - 1:
      return 'none'
    counter += 1
    reader = nums[counter]
  return counter


example_1 = [1, 2, 3, 4, 5, 6, 7, 8]

print(linear_search(example_1, 9))