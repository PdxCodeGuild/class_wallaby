def comp(string_1):
    output = ''
    count = 0
    
    
    for i in range(len(string_1)-1):
        
        if string_1[i] == string_1[i+1]:
            count += 1
        
        elif string_1[i] != string_1[i+1]:
            output += string_1[i]
            count += 1
            
      
    
    
    return output 
    
print(comp('raaainboww'))
  

