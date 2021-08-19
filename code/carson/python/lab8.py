
data = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]

def peak(num):
    '''Returns the indices of peaks. A peak has a lower number on both the left and the right.'''
    num = []
    for i in range(len(data) - 1):
        if data[i] > data[i+1] and data[i] > data[i-1]  :
            num.append(i)
    return num

def valley(num):
    '''Returns the indices of 'valleys'. A valley is a number with a higher number on both the left and the right.'''
    num = []
    for i in range(len(data)-1):
        if data[i] < data[i+1] and data[i] < data[i-1]:
            if i == 0:
                continue
            num.append(i)

    return num

def peaks_and_valleys(num):
    x = peak(i) + valley(i) 
    return x               


num = []

for i in range(len(data)):
    num.append(data[i])


print(peaks_and_valleys(data))