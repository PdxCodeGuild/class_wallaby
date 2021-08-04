import csv

with open('dogs.csv','r', encoding ='utf-8') as file:
    dogs = file.read().split('\n')
    #print(dogs)

with open('dogs.csv', 'a') as file:
    file.write('Labrador, Olivia, 3 years old')

best_in_class = {}


for i in range(len(dogs)):
    if i == 0:
        best_in_class.update({'Herding':dogs[0]})
    elif i == 1:
        best_in_class.update({'Toy':dogs[1]})
    elif i == 2:
        best_in_class.update({'Hound':dogs[2]})
    elif i == 3:
        best_in_class.update({'Non-sporting':dogs[3]})
    elif i == 4:
        best_in_class.update({'Terrier':dogs[4]})
    elif i == 5:
        best_in_class.update({'Working':dogs[5]})
    elif i == 6:
        best_in_class.update({'Sporting':dogs[6]})

#hint: look up dictionary methods, create a line item


best_in_class.update({'Sporting':'Labrador, Olivia, 3 years old'})
print(best_in_class)


#Retrieve a record: ask the user for the winner of the group
search = input("Search for winner by entering the group name: ")
#find the breed in the list, and display its information

if search == "Herding":
    print(dogs[0])
elif search == "Toy":
    print(dogs[1])
elif search == "Hound":
    print(dogs[2])
elif search == "Non-sporting":
    print(dogs[3])
elif search == "Terrier":
    print(dogs[4])
elif search == "Working":
    print(dogs[5])
elif search == "Sporting": 
    print(dogs[6])


#Update a record: ask the user for the contact's name, then for which attribute of the user they'd like to update and the value of the attribute they'd like to set.

update_group_record = input(" Do you want to update the winner? yes/no:  ")
if update_group_record =="yes":
    update_dog_attribute = input("What attribute do you want to update(breed, dog name, age):  ")
    if update_dog_attribute == "breed":
        attribute_change1 = input("Change breed to: ")
        updated_breed = (best_in_class["Herding"].replace("Border Collie", attribute_change1))
        print(updated_breed)
    if update_dog_attribute == "dog name": 
        attribute_change2 = input("Change dog name to: ")
        updated_dogname = (best_in_class["Herding"].replace("Duke", attribute_change2))
        print(updated_dogname)
    if update_dog_attribute == "age":
        attribute_change3 = input("Change age to: ")
        updated_age = (best_in_class["Herding"].replace("3 years old", attribute_change3))
        print(updated_age)

with open('winners.csv', 'w') as new_file:
    new_file.write(updated_breed)

delete_input = input('Do you want to remove the latest update? yes/no: ')
if delete_input == 'yes':
    with open('winners.csv', 'w') as new_file:
        for row in new_file:
            del row[0]
            
            

            
            


#When REPL loop finishes, write the updated contact info to the CSV file to be saved. I highly recommend saving a backup `contacts.csv` because you likely won't write it correctly the first time.
