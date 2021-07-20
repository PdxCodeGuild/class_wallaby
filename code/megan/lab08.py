data = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]

def peaks():
    peaks = []
    for i in range(len(data) - 1):
        if data[i] > data[i + 1] and data[i] > data [i-1]:
            peaks.append(i)
    return peaks
# print(peaks())

def valleys():
    valleys = []
    for i in range(len(data) - 1):
        if data[i] < data[i + 1] and data[i] < data [i-1]:
            if i == 0:
                continue
            valleys.append(i)
    return valleys
# print(valleys())

print(f'''Peaks: {peaks()}
Valleys: {valleys()}
Peaks & valleys: {peaks() + valleys()}''')