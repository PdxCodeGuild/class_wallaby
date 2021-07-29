import string


with open ('tale_of_2_cities.txt', encoding="utf8") as file:
    contents = file.read()

file_name = file.name

"""
file_name = file.name

book = ('tale_of_2_cities.txt')

text = open(book)

books = text.read()
print(books)
"""


def word_counter(file):
    word_count = 0
    words = file.split()
    word_count += len(words)
    return word_count


def char_counter(file):
    char_count = 0
    for char in file:
        if char in string.ascii_letters:
            char_count += 1
    return char_count
          



def sentence_cournter(file):
    sentences = 0
    for ending in file:
         if ending in ['.', '!', '?']:
             sentences += 1
    return sentences

# ARI scale
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




char_in_word = round((char_counter(contents) / word_counter(contents)))


words_per_sentence = round(word_counter(contents) / sentence_cournter(contents))


ARI_tot = round(((4.71 * (char_in_word)) + (0.5 * (words_per_sentence)) - 21.43))
#print(ARI_tot)


print(f'The ARI for {file_name} is {ARI_tot}')
print(f'This corresponds to a {(ari_scale[ARI_tot])["grade_level"]} level of difficulty')
print(f'that is suitable for an average person {(ari_scale[ARI_tot])["ages"]} years old.')

