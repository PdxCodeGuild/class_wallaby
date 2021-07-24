from os import read, write
import re

f = open('mark_twain.txt')  # open the file
contents = f.read()  # read the contents
print(contents)

# Quantity of characters

quantity_of_characters = len(contents)
print(f"count of characters: {quantity_of_characters}")

#Quantity of words
quantity_of_words = len(contents.split())
print(f"count of words: {quantity_of_words}")

# Quantity of sentences
quantity_of_sentences = len(re.findall(r'\w+',contents))
print(f"count of sentences: {quantity_of_sentences}")

equation_part1 = quantity_of_characters // quantity_of_words
multiply1 = equation_part1 *4.71
print(f"character to words : {multiply1}")


equation_part2 = quantity_of_words // quantity_of_sentences
multiply2 = equation_part2 *.5
print(f"words to sentence: {multiply2}")


sum_equation = multiply1 + multiply2 -21.43
print(sum_equation)

roundup_num = round(sum_equation)
print(f"The ARI for Adventures of Huckberry Finn is: {roundup_num}")


ari_scale = {
     1: {'ages':   '5-6', 'grade_level': 'Kindergarten'},
     2: {'ages':   '6-7', 'grade_level':    '1st Grade'},
     3: {'ages':   '7-8', 'grade_level':    '2nd Grade'},
     4: {'ages':   '8-9', 'grade_level':    '3rd Grade'},
     5: {'ages':  '9-10', 'grade_level':    '4th Grade'},
     6: {'ages': '10-11', 'grade_level':    '5th Grade'},
     7: {'ages': '11-12', 'grade_level':    '6th Grade'},
     8: {'ages': '12-13', 'grade_level':    '7th Grade'},
     9: {'ages': '13-14', 'grade_level':    '8th Grade'},
    10: {'ages': '14-15', 'grade_level':    '9th Grade'},
    11: {'ages': '15-16', 'grade_level':   '10th Grade'},
    12: {'ages': '16-17', 'grade_level':   '11th Grade'},
    13: {'ages': '17-18', 'grade_level':   '12th Grade'},
    14: {'ages': '18-22', 'grade_level':      'College'}
}



print(ari_scale[roundup_num])






