
jackalopes = [0, 0]

#initial_population = 2

# reproducing for 4 out of 10 years
# mortality rate = 10 years 

# for loop
# for i in range(len)
'''
for i, jackalope in enumerate(jackalopes):
    # assignment
    jackalopes[i] += 1
    print(jackalopes)
    # check their ages
'''

counter = 0    
while len(jackalopes) < 1000:
    counter+=1
    for i, jackalope in enumerate(jackalopes):
        jackalopes[i] +=1
        if jackalope >= 4 and jackalope <= 8:
            jackalopes.append(0) 
    while 10 in jackalopes:
        jackalopes.remove(10)

print(len(jackalopes))
print(counter)


'''
for len(jackalopes) < 1000:
    if jackalope >= 4 and jackalope <= 8:
        jackalope * 2
    print(type(jackalope))

    # at age 10, remove from list

'''
'''
total_population = 2 
growth_factor = 2
day_count = 0 # Every ? the population is reported
while total_population < 1000:
    total_population *= growth_factor
'''


