
with open('dogs.csv', 'r') as file:
    lines = file.read().split('\n')
    print(lines)