
mtn_range = [1,	2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]


peak_list = []
valley_list = []



for i in range(len(mtn_range)):
    try:
        if  mtn_range[i - 1]  < mtn_range[i]  > mtn_range[i + 1]:
            peak_list.append(i)
        if i == 0:
            continue
        if  mtn_range[i - 1] > mtn_range[i] < mtn_range[i + 1]:
            valley_list.append(i)
    except:
        pass

peaks_and_valleys = peak_list + valley_list

print("Peak", peak_list)

print("Valley", valley_list)

print("Peaks and Valleys",sorted(peaks_and_valleys))



