# Part 1 - Linear Search
'''
nums = [1, 2, 3, 4, 5, 6, 7, 8]

def linear_search(nums, value):
    if value in nums:
        return nums.index(value)
    return False    

index = linear_search(nums, 3) # 2
index = linear_search(nums, 9) # False

print(index)
'''
# Part 2 - Binary Search

nums = [1, 2, 3, 4, 5, 6, 7, 8]

def binary_search(nums, value):
    low = nums[0]
    high = nums[-1]
    while low < high:
        mid = len(nums) / 2
        if mid == value:
            return mid # nums.index(value)
        elif value < mid:
            high = mid 
        elif value > mid:
            low = mid 
        else:
            print('Value not found.')

index = binary_search(nums, 3)
# index = binary_search(nums, 9)

print(index)

# Part 3 - Bubble Sort (optional)

# Part 4 - Insertion Sort (optional)

# Part 5 - Quicksort (optional)