'''     

Let's build a program to manage a list of contacts.
To start, we'll build a CSV ('comma separated values') together
and go over how to load that file. Headers might consist of name, 
favorite fruit, favorite color. Open the CSV, 
convert the lines of text into a list of dictionaries
one dictionary for each user.
The text in the header represents the keys,
the text in the other lines represent the values.


with open('contacts.csv', 'r') as file:
    lines = file.read().split('\n')
    print(lines)

contacts = [
    {'name':'matthew', 'favorite fruit':'blackberries', 'favorite color':'orange'},
    {'name':'sam', 'favorite fruit':'pineapple' ...}
]


'''
names = []
fruit = []
color = []
contacts = []
###dict["names"] = names
#dict["fruit"] = fruit
#dict["color"] = color



with open('contact_list.csv', 'r') as f:
    lines = f.read().split('\n')
    headers = lines[0].split(',')

    #print(lines)
    #print(headers)
    for row in lines[1::]:
        dict = {}
        row = row.split(',')
        #print(row)
        for i, key in enumerate(headers):
            value = row[i]
            dict[key] = value
        contacts.append(dict) 
            #print(key)
            #print(value)
    print(contacts)
        
        
        #names.append(row[0]) 
        #fruit.append(row[1])
        #color.append(row[2])
    
    
    #print(names)
    #print(fruit)
    #print(color)
    
#print(dict)
    

   