# https://github.com/PdxCodeGuild/class_wallaby/blob/main/1%20Python/docs/09%20Lists%20%26%20Tuples.md#list-operations
"""
Access element from list: mylist[i]
Given the list of seasons, print out 'summer'
"""
seasons = ['spring', 'summer', 'fall', 'winter']

# print(seasons[1])

"""
Access element from nested lists: mylist[i][j]
Given the 2D list of seasons, print out 'july'
"""
spring = ['march', 'april', 'may']
summer = ['june', 'july', 'august']
fall = ['september', 'october', 'november']
winter = ['december', 'january', 'febuary']

seasons2d = [spring, summer, fall, winter]

# print(seasons2d[1][1])

"""
Assignment mylist[i] = value
In the list seasons, change 'fall' to 'autumn'
"""
seasons[2] = 'autumn'
# print(seasons)

"""
Assignment to nested lists
Fix the 'febuary' typo in winter THROUGH seasons2d
"""
seasons2d[3][2] = 'february'
# winter[2] = 'february'
# print(seasons2d)
# print(winter)

"""
Loops
Loop over seasons to print out each season
"""
# for season in seasons:
#     print(season)

"""
Loop over seasons to print out each season using range() and len()
"""
# for i in range(len(seasons)):
#     print(seasons[i])

# for i, season in enumerate(seasons):
#     print(i, season)

"""
Nested Loops
Loop over seasons2d AND the nested lists to print out each month
"""
# for season in seasons2d:
#     print(season)
#     for month in season:
#         print(month)

"""
Using range() and len(), loop over seasons2d to print out each month
"""
# for i in range(len(seasons2d)):
#     season = seasons2d[i]
#     for j in range(len(season)):
#         print(season[j])

# for i in range(len(seasons2d)):
#     for j in range(len(seasons2d[i])):
#         print(seasons2d[i][j])

"""
Inclusion: element in mylist
Append: mylist.append(element)
Use in and append to makes sure all the items_to_add are in grocery_list just once
"""
grocery_list = ['apples', 'bananas', 'oranges']
items_to_add = ['bananas', 'blueberries']

# print('bananas' in grocery_list)
# print('blueberries' in grocery_list)
# for fruit in items_to_add:
#     if fruit not in grocery_list:
#         grocery_list.append(fruit)
# print(grocery_list)


# print(grocery_list)

"""
Insert: mylist.insert(index, element)
Add mangos to the top of the list
"""
grocery_list = ['apples', 'bananas', 'oranges']
grocery_list.insert(0, 'mangos')
# print(grocery_list)

"""
Remove: mylist.remove(element)
Remove bananas from the list with .remove()
"""
grocery_list = ['apples', 'bananas', 'oranges']
grocery_list.remove('bananas')
# print(grocery_list)

"""
Pop: mylist.pop(index)
Using .pop(), remove brocolli to fruits and add it to vegetables
"""
fruits = ['apples', 'oranges', 'brocolli']
vegetables = ['potatoes', 'radishes', 'celery']
brocolli = fruits.pop(2)
vegetables.append(brocolli)
# print(vegetables)

"""
Index: mylist.index(element)
Remove oranges from the randomized list with .pop()
"""
from random import shuffle
grocery_list = ['apples', 'bananas', 'oranges']
shuffle(grocery_list) # grocery_list is now randomly shuffled
# print(grocery_list)
index_of_oranges = grocery_list.index('oranges')
grocery_list.pop(index_of_oranges)
# print(grocery_list)

"""
Remove all the mangos from too_many_mangos
"""

too_many_mangos = ['apples', 'mangos', 'bananas', 'mangos', 'blueberries', 'mangos', 'oranges', 'mangos', 'mangos']
# while 'mangos' in too_many_mangos:
#     too_many_mangos.remove('mangos')
# too_many_mangos.remove('mangos')
# print(too_many_mangos)

"""
Slicing
"""
print(too_many_mangos)
# print(too_many_mangos[2::])
# print(too_many_mangos[:2:])
# print(too_many_mangos[::2])
# print(too_many_mangos[1::2])
# print(too_many_mangos[3:5])
print(too_many_mangos[::-1])
too_many_mangos.reverse()
too_many_mangos.sort()
print(too_many_mangos)

# print('hello this is a string'[::-1])
mystring = 'Python'
print(reversed(mystring))  # <reversed object at 0x7fb67b77dd68>
print(list(reversed(mystring)))  # ['n', 'o', 'h', 't', 'y', 'P']
print(sorted(mystring))  # ['P', 'h', 'n', 'o', 't', 'y']
print(mystring)