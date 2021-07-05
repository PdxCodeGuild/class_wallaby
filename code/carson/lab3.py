
ones = ["zero","one ","two ","three ","four ", "five ", "six ",
"seven ","eight ","nine ",] 
teens = ["ten ","eleven ","twelve ", "thirteen ",
 "fourteen ","fifteen ","sixteen ","seventeen ", "eighteen ","nineteen "]
 
tens = ["","", "twenty ","thirty ","forty ", "fifty ","sixty ","seventy ",
"eighty ","ninety "] 

#n = input(f'Please enter a number to change to a word! :): ')
def num(n):
    
  
    a = n%10
    b =  n//10 # double digit

    if n >= 10 and n <= 19: 
        c = teens[n - 10]
    
    elif b >= 1:
        c = tens[b] + ones[a]   #double digit
    
    elif b <= 9: 
        c = ones[a] # single digit
    return c 
   

while True:
    x = input(f'Please pick a number to turn into a phrase or type "done" to quit:  ')
    
    if x == "done":
     break
    
    else:
       
       x = int(x)
       
    print( f' Your number is {num(x)} !')





