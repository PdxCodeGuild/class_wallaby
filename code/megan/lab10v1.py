from csv import DictWriter

with open('contacts.csv', 'r') as f:
    lines = f.read().split('\n')
    # print(lines)
    for row in lines:
        rows = row.split(',')
        # print(rows)

# headers = keys
# rows = values

# keys = {}
contacts_dct = {}   
values = {}
contacts = []

# make first row (headers) the keys
for i in range(len(rows)):
    if i == 0:
        contacts_dct.update({'first name': rows[0]})
    elif i == 1:
        contacts_dct.update({'last name': rows[1]})
    elif i == 2:
        contacts_dct.update({'city': rows[2]})
    elif i == 3:
        contacts_dct.update({'occupation': rows[3]})
# print(keys)

# add all values to list
for row in rows:
    contacts.append(contacts_dct)

print(contacts)







'''
# zip keys and values dictionaries?


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