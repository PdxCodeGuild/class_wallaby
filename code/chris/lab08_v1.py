
data = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]

def peaks(data):
  peak_list = [idx for idx, value in enumerate(data) if ((0 if idx == 0 else data[idx - 1]) < value) and (0 if idx == len(data) - 1 else data[idx + 1] < value)]
  # peak_list = [idx for idx, value in enumerate(data) if ((data[idx-1] or IndexError) < value) and ((data[idx+1] or IndexError) < value)]

  return peak_list

print(peaks(data))
