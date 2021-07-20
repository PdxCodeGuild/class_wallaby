# import pytest # import libraries first

# then import your own modules
from palindrome import check_palindrome
from anagram import check_anagram
from every_permutation import every_permutation


# Test the check_palindrome function
def test_check_palindrome1():
	assert check_palindrome('racecar') == True

def test_check_palindrome2():
	assert check_palindrome('Hannah') == True

def test_check_palindrome3():
	assert check_palindrome('dog') == False

def test_check_palindrome4():
	assert check_palindrome("Go Hang a Salami! I'm a Lasagna Hog!") == True


# Test the check_anagram function
def test_check_anagram1():
	assert check_anagram('dormitory', 'dirty room') == True

def test_check_anagram2():
	assert check_anagram('pizza', 'ice cream') == False

def test_check_anagram2():
	assert check_anagram('Jim Morrison', 'Mr. Mojo Risin') == True


# Test the every_permutation function
def test_every_permutation():
	abc_permutations = [
		'abc',
		'acb',
		'bac',
		'bca',
		'cab',
		'cba'
	]
	assert every_permutation('abc') == abc_permutations
