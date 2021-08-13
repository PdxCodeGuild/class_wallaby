
data = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]

def peaks(data):
  # This was a practice on what I could do with list comprehension. I want to eventually refactor this to be more reader friendly
  peak_list = [
                idx for idx, value in enumerate(data)
                  if ((0 if idx == 0 else data[idx - 1]) < value)
                    and (0 if idx == len(data) - 1
                    else data[idx + 1] < value)
              ]

  return peak_list

def valleys(data):
  valleys_list = []
  for idx, value in enumerate(data):
    if idx > 0 and idx < len(data):
      if data[idx - 1] > value and data[idx + 1] > value:
        valleys_list.append(idx)

  return valleys_list

def peaks_and_valleys(data):
  result_list = peaks(data)
  valleys_list = valleys(data)
  result_list.extend(valleys_list)
  result_list.sort()
  return result_list


print('peaks list:', peaks(data))
print('valleys list:', valleys(data))
print('peaks & valleys', peaks_and_valleys(data))
