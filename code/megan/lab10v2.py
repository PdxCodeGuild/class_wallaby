with open('contacts.csv', 'r') as f:
    lines = f.read().split('\n')
    # print(lines)

contacts_dct = {}
fields = []
contacts = []

for i in range(len(lines)):
    values = lines[i]
    fields.append(values)
    # print(fields)

for row in lines:
    rows = row.split(',')
    # print(rows)
    contacts_dct = {'first name': rows[0], 'last name': rows[1], 'city': rows[2], 'occupation': rows[3]}
    contacts.append(contacts_dct)

# print(contacts)

print('''Welcome to Contacts.

Enter a command:

add - create a new record
find - retrieve a record
edit - update a record
remove - delete a record
view - view all contacts

''')

contacts = []

while True:
    command = input('Enter add, find, edit, or remove to proceed, or enter "exit" to quit: ')
    
    # create a record
    if command == 'add':
        new_contact = {}    
        new_contact['first name'] = input('Enter first name: ')
        new_contact['last name'] = input('Enter last name: ')
        new_contact['city'] = input('Enter city: ')
        new_contact['occupation'] = input('Enter occupation: ')
        fields.append(new_contact)
        print(new_contact)

    # retrieve a record
    elif command == 'find':
        user_query = input('Enter name to search: ')
        if user_query == contacts[0]:
            print(contacts.index(user_query))
        else:
            print(f'No contact {user_query} found.')

    # update a record
    elif command == 'edit':
        user_update = input('Enter name to update: ')
        if user_update == contacts[0]:
            updated_name = contacts.insert(user_update)
            print(f'{updated_name} has been updated in Contacts.')
        else:
            print(f'No contact by {user_update} found.')

    # delete a record
    elif command == 'remove':
        user_delete = input('Enter name to remove: ')
        if user_delete == contacts[0]:
            removed = contacts.pop(user_delete)
            print(f'{removed} has been deleted from Contacts.')
        else:
            print(f'No contact by {user_delete} found.')

    elif command == 'exit':
        break
    
    else:
        print('Please enter a valid command.')
