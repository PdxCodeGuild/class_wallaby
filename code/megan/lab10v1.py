# https://www.w3schools.com/python/python_ref_dictionary.asp

with open('contacts.csv', 'r') as f:
    lines = f.read().split('\n')
    # print(lines)
    for row in lines:
        contacts = row.split(',')
        # print(contacts)

# make first row the keys
# make following rows the values

contacts_dct = {}   
'''
keys = []
values = []
contacts_lst = []
'''
for i in range(len(contacts)):
    if i == 0:
        contacts_dct.update({'name': contacts[0]})
    elif i == 1:
        contacts_dct.update({'lastname': contacts[1]})
    elif i == 2:
        contacts_dct.update({'city': contacts[2]})
    elif i == 3:
        contacts_dct.update({'occupation': contacts[3]})
   
print(contacts_dct) # {'name': 'joni', 'lastname': 'mitchell', 'city': 'ashland', 'occupation': 'doula'}

keys = (list(contacts_dct)) # ['name', 'lastname', 'city', 'occupation']
print(keys)

values = (list())
print(values)

for i in range(len(lines)):
    values

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