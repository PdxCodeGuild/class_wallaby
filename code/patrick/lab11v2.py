lst_1 = [1,2,3,4,5,6,7,8,9,10]
low = lst_1[0]
high = lst_1[-1]
def search_lst(list, object):
    if low < high:
        mid = high/2
        if mid == object:
            return list.index(object)
        elif mid < object:
            mid_1 = mid = high/2
            for i in mid_1:
                return list.index(object)

print(search_lst(lst_1, 8))

        
