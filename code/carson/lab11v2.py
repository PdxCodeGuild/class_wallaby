nums = [1,2,3,4,5,6,7,8]
#n = len(nums)
search = int(input('Enter a number : '))

# def binary_search(list, object, n):
#     low = 0
#     high =  n - 1
#     mid = ((low + high) // 2)
#     while low <= high:
#         if object > high or object < low:
#             return 'Number out of range' 
#         elif mid == object:
#             return list.index(mid)
#         elif object == high:
#             return list.index(high)
#         elif object == low:
#             return list.index(low)
#         else:
#             return 'Unable to find index'

# print(f'Input Number: {search} \n Index: {binary_search(nums, search, n)} ')

# '''2,5,6,7 don't work properly'''


       
            
def binary_search(nums,i):
    first = 0
    print('first', first)
    last = len(nums)-1
    while  first <= last :
        mid = (first + last) // 2
        print('mid', mid)
        guess = nums[mid]
        print('guess',guess)
        if guess == i :
            return i
        elif i < guess:
            last = mid - 1
            print('now last is ', last)
        else:
            first = mid + 1	
    return None

print(binary_search(nums, search))