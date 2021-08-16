# Lab 11: Searching and Sorting

## Part 1 - Linear Search, cite: https://www.youtube.com/watch?v=UldZOLylez4
index_position = -1
def search(linear_search,n):
    i = 0

    while i < len(linear_search):
        if linear_search[i] == n:
            globals()['index_position']=i
            return True
        i = i + 1
    return False


linear_search = [1, 2, 3, 4, 5, 6, 7, 8]
n = 4

if search(linear_search, n):
    print("The linear search found the index position at: ", index_position)
else:
    print("not found")

## Part 2 - Binary Search, cite: https://www.youtube.com/watch?v=DE-ye0t0oxE

#lower_bound_index = 0
#upper_bound_index = 7
#mid_index = (lower_bound_index + upper_bound_index)/2
          # = (0 + 7)/2 
          # = 3
#mid_value = 4

index_position = -1

def search(binary_search,n):
    lower_bound_index = 0
    upper_bound_index = len(binary_search)-1

    while lower_bound_index <= upper_bound_index:
        mid_value = (lower_bound_index + upper_bound_index) // 2
        if binary_search[mid_value]== n:
            globals()['index_position'] = mid_value
            return True
        else:
            if binary_search[mid_value]< n:
                lower_bound_index = mid_value +1
            else:
                upper_bound_index = mid_value

    return False
binary_search = [1, 2, 3, 4, 5, 6, 7, 8]
n =10
if search(binary_search, n):
    print("The binary search found index position at: ", index_position)
else:
    print("Not Found")




