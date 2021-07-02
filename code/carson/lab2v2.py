
ones = ["", "one ","two ","three ","four ", "five ", "six ",
"seven ","eight ","nine ","ten ","eleven ","twelve ", "thirteen ",
 "fourteen ","fifteen ","sixteen ","seventeen ", "eighteen ","nineteen "] 
 
tens = ["","", "twenty ","thirty ","forty ", "fifty ","sixty ","seventy ",
"eighty ","ninety "] 

#n = input(f'Please enter a number to change to a word! :): ')
def num(n):
    
  
    a = n%10
    b =  n//10 # double digit

    if b <= 1: 
        c = ones[a] # single digit
    elif b >= 1: 
        c = tens[b] + ones[a]   #double digit
    return c


print(num(35))


