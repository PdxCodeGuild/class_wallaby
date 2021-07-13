with open('./lab10_list.csv') as file:
    lines = file.read().split('\n')
dict_1 = {}   
names = []
keys = []
output = []
# keys.append(lines[0])

for i in range(len(lines)):
    values = lines[i].title()
    
    names.append(values)



# for keys in keys:
#     x = keys.split(',')
   
#     dict_1[x[0]] = '' 
#     dict_1[x[1]] = ''
#     dict_1[x[2]] = ''

# for y in range(len(names):
#     print(y[1])
#     y = names.split(',')
#     dict_1['names'] = y

for name in names:
    x = name.split(',')  
    dict_1 = {'Name': x[0], 'Favorite Fruit': x[1], 'Favorite Color': x[2]} 
    output.append(dict_1)

print(output)
