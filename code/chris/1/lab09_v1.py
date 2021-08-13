import math

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

filename = 'TheBattleOfLife.txt'

def open_file(filename):
  try:
    f = open(filename, encoding='utf8')
    contents = f.read()
  except (UnicodeDecodeError) as e:
    print('err', e)
  finally:
    f.close()
  return contents

def ARI_scorer(str):
  # num_of_chars
  # num_of_words
  sentences_list = str.split('.')
  for idx, sentence in enumerate(sentences_list):
    sentences_list[idx] = sentences_list[idx].replace('\n', ' ')
    sentences_list[idx] = sentences_list[idx].replace('\ufeff', ' ')
    sentences_list[idx] = sentences_list[idx].replace(',', '')
    sentences_list[idx] = sentences_list[idx].replace(':', '')
    sentences_list[idx] = sentences_list[idx].strip()
  while '' in sentences_list:
    sentences_list.remove('')
  while ' ' in sentences_list:
    sentences_list.remove(' ')
  words_list = ' '.join(sentences_list).split(' ')
  char_len = 0
  for word in words_list:
    char_len += len(word)
  word_len = len(words_list)
  sentence_len = len(sentences_list)



  score = math.ceil((4.71 * (char_len / word_len)) + (0.5 * (word_len / sentence_len)) - 21.43)
  return score

score = ARI_scorer(open_file(filename))
# ARI_scorer(open_file('GA.txt'))

print(f'''
The ARI for {filename} is {score}
This corresponds to a {ari_scale[score]['grade_level']} level of difficulty
this is suitable for an average person {ari_scale[score]['ages']}
''')