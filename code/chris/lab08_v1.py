
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
      print('code runs ', idx)
      if data[idx - 1] > value and data[idx + 1] > value:
        valleys_list.append(idx)

  return valleys_list


print('peaks list:', peaks(data))
print('valleys list:', valleys(data))
