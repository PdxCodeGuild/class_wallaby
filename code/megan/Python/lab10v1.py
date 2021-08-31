with open('contacts.csv', 'r') as f:
    lines = f.read().split('\n')
    # print(lines)

contacts_dct = {}
fields = []
contacts = []

for i in range(len(lines)):
    values = lines[i]
    # print(values)
    fields.append(values)
    # print(fields)

for row in lines:
    rows = row.split(',')
    # print(rows)
    contacts_dct = {'first name': rows[0], 'last name': rows[1], 'city': rows[2], 'occupation': rows[3]}
    # print(contacts_dct)
    contacts.append(contacts_dct)

print(contacts)