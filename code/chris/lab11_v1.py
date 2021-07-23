example_1 = [1, 2, 3, 4, 5, 6, 7, 8]


def linear_search(nums, value):
  counter = 0
  reader = nums[counter]
  while reader != value:
    if counter >= len(nums) - 1:
      return 'none'
    counter += 1
    reader = nums[counter]
  return counter

# print(linear_search(example_1, 9))



def binary_search(nums, value):
  low = 0
  high = len(nums)
  while low < high:
    mid = (low + high) // 2
    if nums[mid] < value:
      low = mid + 1
    elif nums[mid] > value:
      high = mid - 1
    else:
      return mid
  return 'target not found'

# print(binary_search(example_1, 99))

