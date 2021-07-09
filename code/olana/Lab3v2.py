# Cite: https://www.youtube.com/watch?v=-3JxIgmGDEo

digits1 = ["","one", "two", "three","four", "five", "six", "seven", "eight", "nine"]
digits2 = ["ten","eleven","twelve","thirteen","fourteen","fifteen","sixteen","seventeen","eighteen","nineteen"]
digits3 = ["", "","twenty", "thirty","forty","fifty","sixty","seventy","eighty","ninety"]

user_number = int(input("Enter number: "))

digits_place =[0,0,0]
i=0
while user_number > 0:
     digits_place[i]=user_number%10
     i+=1
     user_number =user_number//10
     num = ""

     if digits_place[2]!=0:
          num+=digits1[digits_place[2]]+" hundred "
     #print(digits_place)   
      
if digits_place[1]!=0:
          if (digits_place[1]==1):
               num+=digits2[digits_place[0]]
          else:
               num+=digits3[digits_place[1]]+" "+digits1[digits_place[0]]
else:
     if digits_place[0]!=0:
          num+=digits1[digits_place[0]] 

print(num)

  
