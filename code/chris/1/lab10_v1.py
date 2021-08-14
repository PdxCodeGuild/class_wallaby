with open('planeswalkers.csv', 'r') as file:
  lines = file.read().split('\n')
  file.close()
  fields = lines[0].replace(',', '')
  fields = fields.split(' ')

planeswalkers = []

for lines_idx, line in enumerate(lines):
  data = lines[lines_idx].split(',')

  planeswalker = {}
  if lines_idx != 0:
    for field_idx, field in enumerate(data):
      planeswalker[fields[field_idx]] = field
    planeswalkers.append(planeswalker)

print(planeswalkers)
