sentence = 'Coding is fun.'
for char in sentence:
	print(char)
print(sentence[0])

sentence_list = list(sentence)
print(sentence_list)
sentence_list[-1] = '!'
print(sentence_list)

sentence = ''.join(sentence_list)
print(sentence)

# string.spilt() and strin.join()
# string_test = 'abc.def.ghi.jkl.mno'
# split_string_list = string_test.split('.')
# print('.'.join(split_string_list))