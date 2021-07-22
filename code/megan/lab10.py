with open('contacts.csv', 'r') as f:
    lines = f.read().split('\n')

contacts_dct = {}   

for row in lines:
    # print(row.split(','))
    contacts = row.split(',')
    # print(contacts)

for i range(len(contacts)):
    if i == 0:
        contacts_dct.update({'name': contacts[0]})
    elif i == 1:
        contacts_dct.update({'lastname': contacts[1]})
    



dict.update([])


    
    # contacts_list = []

contacts = dict(zip(contacts))

print(contacts)


'''
for contact in contacts_dct:
    contact.append(contacts_dct)

print(contacts_dct)
'''
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