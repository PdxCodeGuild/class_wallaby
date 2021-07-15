

lst_1 = [1,2,3,4,5,6,7,8,9,10]

def search_lst(list, object):
    if object in list:
        return list.index(object)
    else:
        return False
print(search_lst(lst_1, 3))
