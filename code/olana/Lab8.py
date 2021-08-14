
#Define the following functions:

#1. `peaks` - Returns the indices of peaks. A peak has a lower number on both the left and the right.

#2. `valleys` - Returns the indices of 'valleys'. A valley is a number with a higher number on both the left and the right.

#3. `peaks_and_valleys` - uses the above two functions to compile a single list of the peaks and valleys in order of appearance in the original data.


#cite: https://www.geeksforgeeks.org/python-program-that-prints-the-count-of-either-peaks-or-valleys-from-a-list/
data_list = [1 ,2 ,3 ,4 ,5 ,6 ,7 ,6 ,5 ,4 ,5 ,6 ,7 ,8 ,9 ,8 ,7 ,6 ,7 ,8 ,9]

#peak(x > y < z) or valley(x < y > z).
#for i, name in enumerate(l):
    #print(i, name)
index = 0

valleys =[]
for idx in range(1, len(data_list) - 1):
    if data_list[idx + 1] > data_list[idx] < data_list[idx - 1]:
        index += 1
        valleys.append(idx)
print(f" The valleys are: {valleys}")

peaks =[]
for idx in range(1, len(data_list) - 1):
    if data_list[idx + 1] < data_list[idx] > data_list[idx - 1]:
        index += 1
        peaks.append(idx)

print(f" The peaks are: {peaks}")

peaks_and_valleys =[]
for idx in range(1, len(data_list) - 1):
    if data_list[idx + 1] > data_list[idx] < data_list[idx - 1] or data_list[idx + 1] < data_list[idx] > data_list[idx - 1]:
        index +=1
        peaks_and_valleys.append(idx)
print(f"The peaks and valleys are: {peaks_and_valleys}")







