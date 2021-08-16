def isogram(string):
    string = string.lower()
    letter_list = []
    for x in string:
        if x in letter_list:
            return False
        letter_list.append(x)
        
    return True
        
         

print(isogram("Dermatoglyphics"))