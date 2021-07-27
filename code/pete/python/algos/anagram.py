from string import punctuation

def check_anagram(string1, string2):
	"""Returns True if string1 and string2 are anagrams of each other.
	Otherwise, returns False."""
	string1 = string1.lower()
	string1 = string1.translate(string1.maketrans('', '', punctuation + ' '))
	string2 = string2.lower()
	string2 = string2.translate(string2.maketrans('', '', punctuation + ' '))
	list1 = list(string1)
	list2 = list(string2)
	list1.sort()
	list2.sort()
	if list1 == list2:
		return True
	return False