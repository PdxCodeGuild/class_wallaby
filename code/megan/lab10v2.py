print('''Welcome to Contacts.

Enter a command:

add - create a new record
find - retrieve a record
edit - update a record
remove - delete a record

''')

contacts = []

while True:
    command = input('Enter add, find, edit, or remove to proceed (enter "exit" to quit): ')
    if command == 'exit':
        break
    
    # create a record
    elif command == 'add':
        new_contact = {}    
        new_contact['first name'] = input('Enter first name: ')
        new_contact['last name'] = input('Enter last name: ')
        new_contact['city'] = input('Enter city: ')
        new_contact['occupation'] = input('Enter occupation: ')
        contacts.append(new_contact)
        print(contacts)

    # retrieve a record
    elif command == 'find':
        user_query = input('Enter name to search: ')
        contacts.index(user_query)

    # update a record
    elif command == 'edit':
        user_update = input('Enter name to update: ')
        ...

    # delete a record
    elif command == 'remove':
        user_delete = input('Enter name to remove: ')
        contacts.pop(user_delete)

    else:
        print('Please enter a valid command.')
