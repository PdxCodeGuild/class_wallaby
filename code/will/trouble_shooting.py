'''
Debugging tips
'''

'print and check'
ex1 = 'will'

def divide(num):
    number = int(num)
    return 100 / number

# print(divide(ex1)) 

# Python and most languages will reasonably try to indicate 
# which line the code failed on, sometimes it won't work correctly if the
# code is complicated or long

            ### Terminal Output ###
        #   number = int(num)
        #   ValueError: invalid literal for int() with base 10: 'will'


#########################################################################

# our first and best option when recieving a syntax error or unexpected output
# is to use print()

def divide(num):
    print(num)
    # number = int(num)
    # return 100 / number
# print(divide(ex1))
    ### Terminal Output ###
        # 'will'
#########################################################################

# An often better approach would be to use type as follows

def divide(num):
    print(type(num))
    number = int(num)
    return 100 / number

# print(divide(ex1))
    ### Terminal Output ### 
        # <class 'str'>
####################################################################
# in place of print() we can use assert, which will raise an AssertionError
# if the statement is False
ex5 = 8
def divide(num):
    assert type(num) == int, 'num must be an integer'
    number = int(num)
    return 100 / number
# print(divide(ex5))

    ### Terminal output ### 
    # assert type(num) == int, 'num must be an integer'
    # AssertionError: num must be an integer

'the VScode debugger'
# the built in debugger is amazing for examining your program,
# you can actually see what's happening in that for loop real time instead of waiting on the terminal
ex3 = 359999
import math

def make_readable(seconds):
    hours = math.floor(seconds / 3600)
    string_hours = str(hours)
    remainder = seconds - (hours * 3600)
    minutes = math.floor(remainder / 60 )
    string_minutes = str(minutes)
    seconds = remainder - (minutes * 60)
    string_seconds = str(seconds)
    output_hours = string_hours.zfill(2)
    output_minutes = string_minutes.zfill(2)
    output_seconds = string_seconds.zfill(2)
    return f'{output_hours}:{output_minutes}:{output_seconds}'

# print(make_readable(ex3))

# test1 = 'Do We have A Hashtag'
test2 = 'Codewars Is Nice'
# test3 = 'codewars  is  nice'
def generate_hashtag(s):
        first = s.lower()
        second = first.title()
        words = [word for word in second.split()]
        final_string = '#'+''.join(words) 
        return final_string if 1 <  len(final_string) <= 140 else False

print(generate_hashtag(test2))