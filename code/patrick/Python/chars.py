def compression(string):
    index = 0 # start
    output = "" #returned 
    len_string = len(string) #to make sure we do not get out of range
    while len_string != index:
        count = 1 #first letter is 1
        while index < len_string-1 and string[index] == string[index+1]: #will continue until consecutive letters no longer match. 
            index += 1
            count += 1
        output += str(string[index])  
        output += str(count)
        index += 1
    return output
        
print(compression('rraaainboww'))
















#found the below code from two different sources. Spliced them together and studied it. 

# def compress(string):
#     index = 0 #index 
#     compressed = "" #ouput
#     len_str = len(string) #length of string 
#     while index != len_str: #continue until 
#         count = 1 # first letter starts at 1 and index of 0
#         while (index < len_str-1) and (string[index] == string[index+1]): # Will loop through to see if first letter matches second. 
#             count = count + 1
#             index = index + 1
#         if count == 1: # when current letter does not equal the next. 
#             compressed += str(string[index]) #letter by itself 
#         else:
#             compressed += str(string[index]) + str(count) # letter plus count 
#         index = index + 1
#     return compressed
    
# print(compress('rraaainboww'))
  

