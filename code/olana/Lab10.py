
with open('dogs.csv', 'r') as file:
    dogs = file.read().split('\n')
    #print(dogs)

#hint: look up dictionary methods, create a line item

dogs.append('labrador,large,sporting')
print(dogs)

#Retrieve a record: ask the user for the breed of dog 
search = input("Enter breed name: ")
#find the breed in the list, and display its information

if search == 'standard poodle':
    print(dogs[1])
elif search == 'pug':
    print(dogs[2])
elif search == 'great dane':
    print(dogs[3])
elif search == 'border collie':
    print(dogs[4])
elif search == 'labrador':
    print(dogs[6])

#Ask the user to update the list

update_breed = input("To update the dog's info type enter the breed: ")
update_attributes = input("Which attribute would you like to update, type size or group: ")
if update_attributes == 'size':
    update_size_attributes = input("Update size: ")
    dogs.append(update_size_attributes)
else:
    update_group_attributes = input("Update group: ")



