'''
showdogs_file = open('dogs.csv','r')
for row in showdogs_file:
    print(row.split(',')[0])
'''
with open('dogs.csv','r', encoding ='utf-8') as file:
    dogs = file.read().split('\n')
    print(dogs)

#hint: look up dictionary methods, create a line item

dogs.append('labrador, medium, sporting')
print(dogs)


#Retrieve a record: ask the user for the breed of dog 
#search = input("Enter breed name: ")
#find the breed in the list, and display its information

#results = dogs.get()
#print(results)

'''
if search == 'border collie':
    print(dogs[1])
elif search == 'pug':
    print(dogs[2])
elif search == 'greyhound':
    print(dogs[3])
elif search == 'poodle':
    print(dogs[4])
elif search == 'norwich terrier':
    print(dogs[5])
elif search == 'akita':
    print(dogs[6])
elif search == 'labrador':
    print(dogs[7])
#Ask the user to update the list

update_breed = input("To update the dog's info type enter the breed: ")
update_attributes = input("Which attribute would you like to update, type size or group: ")
if update_attributes == 'size':
    update_size_attributes = input("Update size: ")
    dogs.append(update_size_attributes)
    print(dogs)
else:
    update_group_attributes = input("Update group: ")
    dogs.append(update_group_attributes)

'''
'''
#cite: list_exercises.py
spring = ['march', 'april', 'may']
summer = ['june', 'july', 'august']
fall = ['september', 'october', 'november']
winter = ['december', 'january', 'febuary']

seasons2d = [spring, summer, fall, winter]

print(seasons2d[1][1])

'''
