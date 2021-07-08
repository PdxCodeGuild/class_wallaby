#print(1==1)
#print(True or True or True or True)
#print(False or False or True or True)
# shorthand
#print(1 < 2 < 3) #shorthand  < and > for the below
#print(1 < 2 and 2 < 3)
# == and ! shorthands
#x=1
#y=1
#z=1
#print(x==y==z)

# in and not in
#nums =[1,2,3,4,5]
#print(1 in nums, 6 in nums)

# is, is not
'''
x=5
y=5
print(x==y, x is y)

test ={"a":1, "b":2, "c":3}
keys ={"a","b", "c", "d"}
for key in keys:
    if test.get(key) is not None:
        print(test.get(key))

'''
'''
if True:
    print('it was true')

if 1:
    print("one is True")

'''
#Type Errors
'''
import abc
not_a_list = abc
for num in not_a_list:
    print(num) #for num in not_a_list: TypeError: 'module' object is not iterable
'''
#raise ValueError("This code is not very valuable")
'''
try:
    x = 1 +"1"
    print(x)
except:
    print("An error occurred")

'''

# Exercise 1
'''
teachers = [
    {
    'name': 'Pete',
    'city': 'Portland',
    'job': 'programmer',
    'computer': 'Dell',
},
    {'name': 'Will',
    'city': 'Eugene',
    'job': 'programmer',
    'computer': 'Acer'}

]
keys = ['name', 'city', 'job', 'computer', 'bicycle']
for teacher in teachers:
    print()
    for key in keys:
        try:
            print(f'Their {key} is {teacher[key]}')
        except KeyError:
            print(f"They have no {key}")


'''
# Exercise 2
'''
def add(x, y):
    print(f'{x} + {y}')
    return x + y

test_inputs = [
    (2, 2),
    ('2', '2'),
    ('two', 2),
    (2, '2'),
]

for nums in test_inputs:
    try:
        result = add(nums[0], nums[1])
        print(result)
    except TypeError:
        print('a TypeError has occurred')

'''

