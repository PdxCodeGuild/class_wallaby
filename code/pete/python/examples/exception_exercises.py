# Exercise 1
teachers = [
    {
        'name': 'Pete',
        'city': 'Portland',
        'job': 'programmer',
        'computer': 'Dell',
    },
    {
        'name': 'Will',
        'city': 'Eugene',
        'job': 'programmer',
        'computer': 'Acer'
    }

]
keys = ['name', 'city', 'job', 'computer', 'bicycle']
for teacher in teachers:
    print()
    for key in keys:
        try:
            print(f'Their {key} is {teacher[key]}')
        except KeyError:
            print(f"They have no {key}")

# Exercise 2
def add(x, y):
    print(f'{x} + {y}')
    return int(x) + int(y)

test_inputs = [
    (2, 2),
    ('2', '2'),
    (2, '2'),
    ('two', 2),
]

for nums in test_inputs:
    try:
        result = add(nums[0], nums[1])
        print(result)
    except TypeError:
        print('a TypeError has occured')
    except ValueError:
        print("Please enter a valid number")
    print()