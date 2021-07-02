# https://github.com/PdxCodeGuild/class_wallaby/blob/main/1%20Python/docs/09%20Lists%20%26%20Tuples.md#list-operations
"""
Access element from list: mylist[i]
Given the list of seasons, print out 'summer'
"""
seasons = ['spring', 'summer', 'fall', 'winter']

# print(seasons)

"""
Access element from nested lists: mylist[i][j]
Given the 2D list of seasons, print out 'july'
"""
spring = ['march', 'april', 'may']
summer = ['june', 'july', 'august']
fall = ['september', 'october', 'november']
winter = ['december', 'january', 'febuary']

seasons2d = [spring, summer, fall, winter]

# print(seasons2d)

"""
Assignment mylist[i] = value
In the list seasons, change 'fall' to 'autumn'
"""

# print(seasons)

"""
Assignment to nested lists
Fix the 'febuary' typo in winter THROUGH seasons2d
"""

# print(seasons2d)

"""
Loops
Loop over seasons to print out each season
"""

"""
Loop over seasons to print out each season using range() and len()
"""

"""
Nested Loops
Loop over seasons2d AND the nested lists to print out each month
"""

"""
Using range() and len(), loop over seasons2d to print out each month
"""

"""
Inclusion: element in mylist
Append: mylist.append(element)
Use in and append to makes sure all the items_to_add are in grocery_list just once
"""
grocery_list = ['apples', 'bananas', 'oranges']
items_to_add = ['bananas', 'blueberries']

# print(grocery_list)

"""
Insert: mylist.insert(index, element)
Add mangos to the top of the list
"""
grocery_list = ['apples', 'bananas', 'oranges']
# print(grocery_list)

"""
Remove: mylist.remove(element)
Remove bananas from the list with .remove()
"""
grocery_list = ['apples', 'bananas', 'oranges']
# print(grocery_list)

"""
Pop: mylist.pop(index)
Using .pop(), remove brocolli to fruits and add it to vegetables
"""
fruits = ['apples', 'oranges', 'brocolli']
vegetables = ['potatoes', 'radishes', 'celery']

"""
Index: mylist.index(element)
Remove oranges from the randomized list with .pop()
"""
from random import shuffle
grocery_list = ['apples', 'bananas', 'oranges']
shuffle(grocery_list) # grocery_list is now randomly shuffled
# print(grocery_list)

"""
Remove all the mangos from too_many_mangos
"""

too_many_mangos = ['apples', 'mangos', 'bananas', 'mangos', 'blueberries', 'mangoes', 'oranges', 'mangos', 'mangos']
