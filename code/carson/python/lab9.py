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

#f = open('dracula.txt')  # open the file
#contents = f.read()  # read the contents
#print(contents)

title = 'dracula.txt'
with open('dracula.txt', 'r',encoding = 'utf-8') as f:
    contents = f.read()    
    sentence = (len(contents.split('. '))) -1
    word = len(contents.split())
    characters = len([list(line.rstrip()) for line in contents])
    score = characters/word * 4.71
    #print(score)
    score1 = word/sentence*.5 - 21.43
    #print(score1)
    score = round(score + score1)
   
    if score >= 14:
        score = 14
        #print(score)
         
    print(f'The ARI for {title} is {score} \nThis corresponds to a {ari_scale[score]["grade_level"]} level of difficulty \nThat is suitble for an average person  {ari_scale[score]["ages"]} years old. ')    
  
   

    
    
    
    
    
    #print(f"word : {word} ")
    #print(f'sentence : {sentence}')
    ##print(f'characters : {characters}')
    #print(f'score : {score}')
   

   