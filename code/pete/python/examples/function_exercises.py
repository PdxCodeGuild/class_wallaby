# nums1 = [1,2,3,4,5]
# nums2 = [2,3,4,5,6]
# nums3 = [3,4,5,6,7]

# def double_nums_in_list(nums):
#     for i in range(len(nums)):
#         nums[i] *= 2

# double_nums_in_list(nums1)
# double_nums_in_list(nums2)
# double_nums_in_list(nums3)
# print(nums1, nums2, nums3)

def say_hello(first_name='no first name', last_name='no last name'):
    print('Hello ' + first_name + ' ' + last_name)

# fn = input('what is your first name? ') # I typed 'pete'
# ln = input('what is your last name? ') # I typed 'jones'
# say_hello(fn, ln) # fn is 'pete', ln is 'jones'
# say_hello() # fn is 'pete', ln is 'jones'
# say_hello('pete')
# say_hello(last_name='jones')
# say_hello(first_name='pete', 'jones') # cannot use positional argument after keyword argument
# say_hello(fn, ln) # fn is 'pete', ln is 'jones'

def temperature_report(temperature):
    if temperature < 60:
        return 'cold'
    if temperature < 70:
        return 'warm'
    if temperature < 80:
        return 'pretty warm'
    if temperature < 90:
        return 'hot'
    return "wow it's so hot!"

# print(temperature_report(59))
# print(temperature_report(73))
# print(temperature_report(99))


"""
EXERCISE 1
Write an add function that returns the sum of two numbers
"""
def add(x, y):
    return x + y
    # i = x + y
    # return i

print(add(1, 2)) # 3
print(add(3, 7)) # 10

"""
EXERCISE 2
Write a function that capitalizes the first letter of every word in a string
"""
def capitalize(message):
    return message.title()

print(capitalize('capitalize this message')) # Capitalize This Message

"""
EXERCISE 3
Write an add function that takes in *args and returns the sum of all numbers
"""
def add_plus(*nums):
    # print(nums)
    # start a total counter?
    total = 0
    for num in nums:
        # add each num to the total
        total += num
    return total


print(add_plus(1, 2, 3, 4, 5, 6)) # 21

def kwarg_test(**kwargs):
    print(kwargs)

print()
kwarg_test()
print()
kwarg_test(name='pete')
print()
kwarg_test(instructor='pete', ta='will', class_mascot='wallaby')

def arg_test(*args):
    print(args)
    for arg in args:
        print(arg, end=' ')

# arg_test('hellow', 1, 5, 8, ['s', 1], {'a': 1})

def gimme_abc():
    return 'a', 'b', 'c'

abc = gimme_abc()
print(abc)

a, b, c = gimme_abc()
print(a)
print(b)
print(c)

a = lambda x,y: x + y
print(a(5,4)) # 9
def add(x, y):
    return x + y

s = lambda x,y: x - y
print(s(5,4)) # 1
def subtract(x, y):
    return x - y


def fake_pick6():
    return [23, 45, 65, 12, 8, 42]