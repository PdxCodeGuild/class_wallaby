import copy

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

decon_data = copy.copy(data)
graph_matrix = [copy.copy(decon_data)]

while_tracker = True
peaks_results = peaks(data)

while while_tracker:
  while_tracker = False
  for idx in range(len(decon_data)):
    if decon_data[idx] > 0:
      while_tracker = True
      decon_data[idx] -= 1

  graph_matrix.append(copy.copy(decon_data))

for idx, row in enumerate(graph_matrix):
  print(idx)
  for jdx, column in enumerate(row):
    if jdx > 6 and jdx < 14 and column == 0 and idx <= 6:
      row[jdx] = 'W'
    elif jdx > 14 and (jdx < (len(row) - 1)) and column == 0 and idx <= 8:
      print(idx)
      row[jdx] = 'W'

  print(row)


for row in reversed(graph_matrix):
  for idx, value in enumerate(row):
    if row[idx] == 0:
      row[idx] = ' '
    elif row[idx] == 'W':
      row[idx] = 'O'
    else:
      row[idx] = 'X'
  row = '  '.join(row)
  print(f'''       {row}''')

print(f'''Data: {data}

Peaks: {peaks(data)}
Valleys: {valleys(data)}
''')

