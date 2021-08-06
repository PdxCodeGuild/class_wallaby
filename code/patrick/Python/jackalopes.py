

jack = [0,0]
years = 0
while len(jack) <= 1000:
    years += 1
    for i, j in enumerate(jack):
        jack[i] += 1 
    for i, j in enumerate(jack):
        #jack[i] += 1    

        if jack[i] >= 4 and jack[i] <= 8:
            jack.append(0)

                
    
        while 10 in jack: 
            jack.remove(10)
            
        
print(years)
print(f'Population: {i}')
print(jack)
