import string

ROT13 = {}
user_input = input('Please enter an string to be encoded: ')


encoded_str = ''

alphabet_letter = string.ascii_letters
letter_list = [char for char in alphabet_letter]





for i, char in enumerate(alphabet_letter):
  
  ROT13[char] = alphabet_letter[(i + 13) % 26]
'''
<!-- To wrap around from index 25 to 0 use modulus %26 to give you the remainder -->
'''

for i, char in enumerate(user_input):
  
  encoded_str += ROT13[char]

print(f"\nYour new encoded string is: {encoded_str}")
