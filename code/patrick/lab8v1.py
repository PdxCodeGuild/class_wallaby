data_1 = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]

lst_1 = []

for i in range(len(data_1)):
    lst_1.append(data_1[i])

def peaks(lst):
    lst = []
    for i in range(len(data_1) - 1):
        if data_1[i] > data_1[i+1] and data_1[i] > data_1[i-1]  :
            lst.append(i)
    return lst

def valleys_1(lst):
    lst = []
    for i in range(len(data_1)-1):
        if data_1[i] < data_1[i+1] and data_1[i] < data_1[i-1]:
            lst.append(i)            
    return lst


def combined(lst):
    x = peaks(i) + valleys_1(i)                
    return x
    

print(valleys_1(data_1))


