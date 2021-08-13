nums = [1,2,3,4,5,6,7,8]
#n = len(nums)
search = int(input('Enter a number : '))

def binary_search(nums, i):
  low = 0
  high = len(nums)
  while low < high:
    mid = (low + high) // 2
    if nums[mid] < i:
      low = mid + 1
    elif nums[mid] > i:
      high = mid - 1
    else:
      return mid
  return 'Unable to find index'
  
print(binary_search(nums, search))