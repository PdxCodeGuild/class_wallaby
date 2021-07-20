import re

test_paragraph = 'This is a test paragraph.  Does it have multiple sentences?  It sure does!  Does it have more than just periods at the end of sentences?  You bet!'

# sentences = test_paragraph.split('.?!')
sentences = re.split(r'\.|\?|!', test_paragraph)

print(sentences)
print(len(sentences))
