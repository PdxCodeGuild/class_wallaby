# Exercise 1
teachers = [
    {
    'name': 'Pete',
    'city': 'Portland',
    'job': 'programmer',
    'computer': 'Dell',
}

]
keys = ['name', 'city', 'job', 'computer']
for teacher in teachers:
    for key in keys:
        print(f'Their {key} is {teacher[key]}')


# Exercise 2
def add(x, y):
    return x + y

test_inputs = [
    (2, 2),
    ('2', '2'),
    ('two', 2),
    (2, '2'),
]

for nums in test_inputs:
    result = add(nums[0], nums[1])
    print(result)