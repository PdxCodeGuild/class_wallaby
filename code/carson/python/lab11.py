
all = [1, 2, 3, 4, 5, 6, 7, 8]

def linear_search(all, object):
    if object in all:
        return all.index(object)
    else:
        return False
index = linear_search(all, 3)

print(index) # 2




