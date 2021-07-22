# Part 1 - Linear Search

nums = [1, 2, 3, 4, 5, 6, 7, 8]

def linear_search(nums, value):
    if value in nums:
        return nums.index(value)
    return False    

index = linear_search(nums, 3) # 2
index = linear_search(nums, 9) # False

print(index)

# Part 2 - Binary Search

nums = [1, 2, 3, 4, 5, 6, 7, 8]

def binary_search(nums, value):
  low = 0
  high = -1
  while low < high:
      ...

index = linear_search(nums, 3)
index = linear_search(nums, 9)

print(index)

# Part 3 - Bubble Sort



# Part 4 - Insertion Sort (optional)

# Part 5 - Quicksort (optional)