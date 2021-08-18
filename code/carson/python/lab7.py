# rot =[
# 'n','o','p','q','r','s','t','u','v','w','x','y','z','a','b','c','d','e','f','g','h','i','j','k','l', 'm',]
# #print(rot)
# abc = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',]
# #print(abc)

# #print(letters)
# #word =['car']
# #l = word.split()

# #print(word)

# for letter in abc:
#    number =[]
#    number = ord(letter), chr(ord(letter))
# print(number)
    #num = (number,letter)
    #print(num)
    #for  in abc:
        #all = 


    #cypher = rot[number]
#print(cypher)
 

import string

abc = string.ascii_lowercase
print(abc)
user = input("Welcome ! please enter a word to be encrypted : ")
dict = {}
all = ''

for i, char in enumerate(abc):
  dict[char] = abc[(i + 13) % 26]

for i, char in enumerate(user):
  all += dict[char]

print(f"ROT13 code: {all}")

