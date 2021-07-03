# < and > shorthand
# print(1 < 2 < 3)
# print(1 < 2 and 2 < 3)

# == and != shorthands
# x = 1
# y = 1
# z = 1
# print(x == y == z)
# x = 1
# y = 2
# z = 3
# print(x == y == z)

# in and not in
# nums = [1, 2, 3, 4, 5]
# print(1 in nums, 6 in nums)
# print(1 not in nums, 6 not in nums)
# from string import ascii_lowercase
# print(ascii_lowercase)
# print('a' in ascii_lowercase, 'A' in ascii_lowercase)
# print('ab' in ascii_lowercase, 'ac' in ascii_lowercase)

# is and is not
# x = 5
# y = 5
# print(x == y, x is y, x is 1)
# print(id(x), id(y), id(1))
test = {'a': 1, 'b': 2, 'c': 3}
keys = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
for key in keys:
    if test.get(key) is not None:
        print(test.get(key))
    else:
        print(key + ' not in test dictionary')