with open('contacts.csv', 'r') as f:
    lines = f.read().split('\n')
    
for row in lines:
    print(row.split(','))

# turn into a list of dictionaries
contacts = [dict()]

print(contacts)


# contacts = [
#     {'first name': '', 'last name': '', 'city': '', 'occupation': ''},
#     {'name': '', 'city': '', 'occupation': ''},
#     {'name': '', 'city': '', 'occupation': ''},
#     {'name': '', 'city': '', 'occupation': ''},
# ]

# Version 2: CRUD REPL

# Version 3: (work backwards)