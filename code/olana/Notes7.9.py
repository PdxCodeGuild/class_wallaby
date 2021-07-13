#List comprehensions

dogs = ['shia', 'raja']


dog_facts =[]
'''
for dog in dogs:
    dog =dog.capitalize()
    dog_facts.append(f"{dog} is a good boy.")
print(dog_facts)

'''

dog_facts = [f"{dog.capitalize} is a good boy." for dog in dogs]
print(dog_facts)