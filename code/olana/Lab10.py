with open('dogs.csv','r', encoding ='utf-8') as file:
    dogs = file.read().split('\n')
    #print(dogs)

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
print(best_in_class)

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
elif search == "Sporting": # bug
    print(dogs[6])


#Update a record: ask the user for the contact's name, then for which attribute of the user they'd like to update and the value of the attribute they'd like to set.

update_group_record = input(" To update the winner, please enter the group name: ")
update_dog_attribute = input('Change attributes: ' )

