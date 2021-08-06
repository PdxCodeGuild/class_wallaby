lst_1 = [1,2,3,4,5,6,7,8,9,10]
x = len(lst_1)
tgt_num = int(input('Enter the number you wish to find the index of: '))
def search_lst(list, object, x):
    low = lst_1[0]
    high = lst_1[x-1]
    mid = ((low + high) // 2)
    while low <= high:
        if object > high or object < low:
            return 'Target out of range!' 
        elif mid == object:
            return list.index(mid)
        elif object == high:
            return list.index(high)
        elif object == low:
            return list.index(low)
        elif mid < object:
            low = mid+1
            continue
        elif mid > object:
            high = mid-1
            continue
        else:
            return None

print(f'The target number of {tgt_num} has an index of {search_lst(lst_1, tgt_num, x)} in the current list.')

        
