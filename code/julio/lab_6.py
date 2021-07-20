#------------------------------------------------------------------------#
def validate_credit_card(cc_num):

    ccnum_2 = [ int(x)  for x in cc_num ]
    num_ver = ccnum_2.pop(-1)
    ccnum_2.reverse()
#------------------------------------------------------------------------#
    for i in range(0, len(ccnum_2), 2):
       ccnum_2[i] *= 2
       
    for i in range(len(ccnum_2)):
        if ccnum_2[i] > 9:
            ccnum_2[i] -=  9

    total = str(sum(ccnum_2))
    if total[1] == str(num_ver):
        return True

    return False
#------------------------------------------------------------------------#
print("#----------------------------------------------#")
cc_num = input ("enter 16 digit CC number: ")
print("#----------------------------------------------#")
if validate_credit_card(cc_num):
    print("#----------------------------------------------#")
    print("valid!")
    print("#----------------------------------------------#")
else:
    print("invalid")
print("#----------------------------------------------#")
#------------------------------------------------------------------------#