with open('cities.csv', 'r') as f:
    data = f.read().split('\n')
    for row in data:
        print(row.split(','))

# turn into a list of dictionaries
[
    {'name': '', 'city': '', 'occupation': ''},
    {'name': '', 'city': '', 'occupation': ''},
    {'name': '', 'city': '', 'occupation': ''},
    {'name': '', 'city': '', 'occupation': ''},
]

# Version 2: CRUD REPL

# Version 3: (work backwards)