"""
Escape Sequences
"""
# # print('hello what's your name?') # SyntaxError
# print('hello what\'s your name?\\')
# print("this is one sentence\n\nthis is another")

# print('you can print unicode symbols: \u4957')
# print('\u7766, \u1337, \u1775')

# import string

# for letter in string.ascii_lowercase:
# 	print(ord(letter), chr(ord(letter)))

# test = 'hello world'
# print(test.replace('hello', 'goodbye'))
# print(test)
# print(id(test)) #
# print()

# # strings are immutable test below is a completely
# # different variable than test above
# test += '!' 
# print(test)
# print(id(test))


"""
Strip
"""
# raw_string = """

# 	test stuff right here
# more test stuff


# things
# stuff 

# """
# print(raw_string)
# print('-'*80)
# print(raw_string.strip())

# print('\n' + '-'*80 + '\n')

# raw_string2 = """---------------------------
# this is the text you want
# ----------------"""

# print(raw_string2)
# print('-'*80)
# print(raw_string2.strip('-'))

# print('\n' + '-'*80 + '\n')
from string import punctuation
# print(punctuation)

# raw_string3 = "#$^&()(^%!$%^&*((*&^importanttext@#$%^&*()(*&"
# print(raw_string3)
# print('-'*80)
# print(raw_string3.strip(punctuation))


"""
Split
"""
sentence = 'the weather was nice today'
print(sentence)
print(sentence.split())
sentence_list = sentence.split('a')
print(sentence_list)
print('a'.join(sentence_list))

# sentence2 = 'it was super sunny because it\'s summer'
# print(sentence2)
# print(sentence2.split('su'))