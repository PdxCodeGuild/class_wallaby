nums = [1,2,3,4,5,6,7,8]
n = len(nums)
search = int(input('Enter a number : '))

def binary_search(list, object, n):
    low = nums[0]
    high = nums[n-1]
    mid = ((low + high) // 2)
    while low <= high:
        if object > high or object < low:
            return 'Number out of range' 
        elif mid == object:
            return list.index(mid)
        elif object == high:
            return list.index(high)
        elif object == low:
            return list.index(low)
        else:
            return 'Unable to find index'

print(f'Input Number: {search} \n Index: {binary_search(nums, search, n)} ')

'''2,3,5,6,7 don't work properly'''