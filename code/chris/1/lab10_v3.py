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

main_input = input('''
1) Add
2) Display
3) Update/edit
4) Delete
''')

if main_input == '1':
  new_planeswalker = {}
  new_planeswalker['name'] = input('Planeswalker name: ')
  new_planeswalker['race'] = input('race: ')
  new_planeswalker['affinity'] = input('affinity: ')
  new_planeswalker['age'] = input('age: ')
  new_planeswalker['power'] = input('power: ')
  planeswalkers.append(new_planeswalker)
  print(planeswalkers)

if main_input == '2':
  display_input = input('Enter planeswalker\'s name: ')
  for planeswalker in planeswalkers:
    if planeswalker['name'] == display_input.title():
      print(planeswalker)

if main_input == '3':
  update_input = input('Enter planeswalker\'s name: ')
  attr_input = input('name, race, affinity, age, or power? ')
  new_input = input(f'change {attr_input} to: ')
  for planeswalker in planeswalkers:
    if planeswalker['name'] == update_input.title():
      planeswalker[attr_input] = new_input.title()
      print(planeswalker)

if main_input == '4':
  delete_input = input('Enter planeswalker\'s name to be deleted ')
  for idx, planeswalker in enumerate(planeswalkers):
    if planeswalker['name'] == delete_input.title():
      deleted = planeswalkers.pop(idx)
  if deleted:
    print(f'{deleted} has been removed')
  else:
    print(f'No planeswalker named {delete_input} found')


with open('test.csv', 'w') as file:
  new_file_str = 'name, race, affinity, age, power\n'
  for planeswalker in planeswalkers:
    for idx, key in enumerate(planeswalker):
      if idx != len(planeswalker) - 1:
        new_file_str += planeswalker[key]
        new_file_str += ','
      else:
        new_file_str += planeswalker[key]
        new_file_str += '\n'

  file.write(new_file_str)
  file.close()