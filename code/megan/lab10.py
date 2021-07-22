with open('contacts.csv', 'r') as f:
    lines = f.read().split('\n')
    
for row in lines:
    # print(row.split(','))
    contacts = row.split(',')
    print(contacts)

contacts = {first_name: last_name}

# dictionary conversions
# dict comprehensions

# turn into a list of dictionaries
# print(dict(contacts))

# contacts = [dict()]
# contacts = []

# print(contacts)


# contacts = [
#     {'first name': '', 'last name': '', 'city': '', 'occupation': ''},
#     {'name': '', 'city': '', 'occupation': ''},
#     {'name': '', 'city': '', 'occupation': ''},
#     {'name': '', 'city': '', 'occupation': ''},
# ]

# Version 2: CRUD REPL

# Version 3: (work backwards)