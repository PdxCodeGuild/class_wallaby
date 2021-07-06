# https: // github.com/PdxCodeGuild/class_wallaby/blob/main/1 % 20Python/docs/11 % 20Dictionaries.md

miles_morales = {
    'superhero': 'Spider-Man',
    'age': 17,
    'home': 'New York City',
    'family': ['Jefferson Davis', 'Rio Morales'],
    'occupation': 'student'
}

"""
Access: dict[key] or dict.get(key)
Access the 'superhero' key to print Miles' superhero name
"""
# print(miles_morales['superhero'])
# print(miles_morales['abilities'])
# print(miles_morales.get('superhero'))
# print(miles_morales.get('abilities'))

"""
Update: dict[key] = value
Happy Birthday Miles 🎂
Increase Miles' age by 1
"""
miles_morales['age'] += 1
# print(miles_morales)

"""
Add Miles' uncle, Aaron Davis, to the family value
"""
miles_morales['family'].append('Aaron Davis')
# print(miles_morales)

"""
Add key/value pair: dict[key] = value
Add more info to the miles_morales dictionary
"""

miles_morales['height'] = 68
miles_morales['abilities'] = ['invisibility', 'crawling on walls']
# miles_morales['abilities'].append('crawling on walls')
miles_keys = miles_morales.keys()
print(miles_keys)
# for key in miles_keys:
#     print(f'{key} is {miles_morales[key]}')
miles_items = miles_morales.items()
for key, value in miles_items:
    print(f'{key} is {value}')