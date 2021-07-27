from string import punctuation

def check_palindrome(string):
	"""Returns True if string is a palindrome.
	Otherwise, returns False."""
	string = string.lower()
	string = string.translate(string.maketrans('', '', punctuation + ' '))
	reversed_string = string[::-1]
	if string == reversed_string:
		return True
	return False