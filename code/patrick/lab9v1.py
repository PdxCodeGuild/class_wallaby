import math
text_1 = open('dracula.txt')
book = text_1.read()

def ari_counter(text):
    words = len(text.split())
    sentences = (len(text.split('. '))) -1
    text = text.replace('.', ' ')
    characters = (len(text) - text.count(' '))
    ari_score = 4.71*(characters/words)+.5*(words/sentences)-21.43
    print("words:",words)
    print('sentences',sentences)
    print('characters', characters)

    print(ari_score)
    if ari_score >= 14:
        ari_score = 14
    return math.ceil(ari_score)
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

print(ari_counter(book))