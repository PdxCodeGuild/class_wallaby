jackalopes = [0, 0]

counter = 0    

while len(jackalopes) < 1000:
    counter += 1
    for i, jackalope in enumerate(jackalopes):
        jackalopes[i] +=1
        if jackalope >= 4 and jackalope <= 8:
            jackalopes.append(0) 
    while 10 in jackalopes:
        jackalopes.remove(10)

print(len(jackalopes))
print(counter)