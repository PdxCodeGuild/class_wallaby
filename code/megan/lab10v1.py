with open('contacts.csv', 'r') as f:
    lines = f.read().split('\n')
    # print(lines)
    for row in lines:
        headers = row.split(',')
        # print(contacts)

keys = {}   
values = {}
contacts = []

# make first row (headers) the keys
for i in range(len(headers)):
    if i == 0:
        keys.update({'first name': headers[0]})
    elif i == 1:
        keys.update({'last name': headers[1]})
    elif i == 2:
        keys.update({'city': headers[2]})
    elif i == 3:
        keys.update({'occupation': headers[3]})
# print(keys)

# make following rows the values


# zip keys and values dictionaries?

print(contacts)



'''
keys = (list(contacts)) # ['name', 'lastname', 'city', 'occupation']
print(keys)

values = []



values = (list())
print(values)

for i in range(len(lines)):
    values = lines[i]
    keys.append(values)

contacts_lst = [] 

contacts.append(contacts_dct)

# append or zip?

# zipped = zip(numbers, letters)




dict.update({'key': values[i]})


    
    # contacts_list = []

contacts = dict(zip(contacts))




for contact in contacts_dct:
    contact.append(contacts_dct)

print(contacts_dct)
 
# turn into a list of dictionaries

# zip + list (or dictionary?) comprehension



# dictionary conversions
# dict comprehensions

# print(dict(contacts))

# contacts = [dict()]
# contacts = []

# contacts = [
#     {'first name': '', 'last name': '', 'city': '', 'occupation': ''},
#     {'name': '', 'city': '', 'occupation': ''},
#     {'name': '', 'city': '', 'occupation': ''},
#     {'name': '', 'city': '', 'occupation': ''},
# ]

# Version 2: CRUD REPL

# Version 3: (work backwards)
'''