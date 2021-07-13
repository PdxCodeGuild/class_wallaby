with open('lab10_list.csv') as file:
    lines = file.read().split('\n')
dict_1 = {}   
names = []
keys = []

keys.append(lines[0])

for i in range(1, len(lines)):
    values = lines[i]
    names.append(values)
print(keys)
print(names)
