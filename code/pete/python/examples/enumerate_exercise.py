# days = ['monday', 'tuesday', 'wednesday', 'thurdsay', 'friday', 'saturday', 'sunday']

# for day in days: # for element in list loop
#     print(day)

# for i in range(len(days)): # for index in list loop
#     print(i)

# for i in range(len(days)): # for index in list AND element
#     print(i, days[i])

# for i, day in enumerate(days):
#     print(i, day)

"""
ENUMERATE EXERCISE
Using enumerate, make a dictionary where the letters are keys and the numbers are values.
"""

keys = ['a', 'b', 'c', 'd', 'e']
values = [1, 2, 3, 4, 5]
letters_and_numbers_dict = {}
for i, letter in enumerate(keys):
    print(i, letter)
    letters_and_numbers_dict[letter] = values[i]

print(letters_and_numbers_dict)
# {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}