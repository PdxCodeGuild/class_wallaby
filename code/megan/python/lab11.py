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
    low = nums[0]
    high = nums[-1]
    while low < high:
        mid = (low + high) // 2
        if value < nums[mid]:
            high = mid - 1
        elif value > nums[mid]:
            low = mid + 1
        else:
            return mid
    print('Value not found.')

index = binary_search(nums, 3) # 2
# index = binary_search(nums, 9) # Value not found. None.

print(index)

# Part 3 - Bubble Sort (optional)

# Part 4 - Insertion Sort (optional)

# Part 5 - Quicksort (optional)