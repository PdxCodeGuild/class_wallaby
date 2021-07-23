from string import punctuation, whitespace
from re import split
from math import ceil

class ARI:
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

	def __init__(self, file_path):
		"""given a filepath, will instantiate an object that can compute 
		the ARI (automated readability index) of a text"""
		self.file_path = file_path
		self.text = self.read_file()
		self.ari = self.calc_ari()

	def read_file(self):
		"""reads the text file and returns that text as a string"""
		with open(self.file_path, 'r', encoding='utf-8') as f:
			# print(type(f))
			text = f.read()
		return text
	 
	def calc_ari(self):
		"""calculates the ARI of the text and returns that integer"""

		characters = self.text.translate(str.maketrans('', '', punctuation + whitespace))
		print(characters)
		num_of_characters = len(characters)

		words = self.text.translate(str.maketrans('', '', punctuation)).split()
		print(words)
		num_of_words = len(words)

		sentences = split(r"\.|!|\?", self.text)
		print(sentences)
		num_of_sentences = len(sentences)
		

		self.num_of_characters = num_of_characters
		self.num_of_words = num_of_words
		self.num_of_sentences = num_of_sentences
		print(num_of_words, num_of_characters, num_of_sentences)

		ari = ceil(4.71 * (num_of_characters / num_of_words) + 0.5 * (num_of_words / num_of_sentences) - 21.43)
		if ari > 14:
			ari = 14

		return ari
	
	def print_ari_info(self):
		"""prints out ARI info for the text"""
		ari_dict = self.ari_scale.get(self.ari)
		print(
f"""--------------------------------------------------------

The ARI for {self.file_path} is {self.ari}
This corresponds to a {ari_dict['grade_level']} level of difficulty
that is suitable for an average person {ari_dict['ages']} years old.

--------------------------------------------------------"""
		)