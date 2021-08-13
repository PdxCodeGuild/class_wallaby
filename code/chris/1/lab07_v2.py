import string
raw_str_input = input('\nEnter string to be encoded: ')
rot_input = int(input('\nEnter amount of cipher rotation(0 is default): '))
encoded_str = ''
alphabet = string.ascii_lowercase
alphabet_list = [char for char in alphabet]
cipher_dict = {}

for i, char in enumerate(alphabet_list):
  cipher_dict[char] = alphabet_list[(i + (rot_input or 13)) % 26]

for i, char in enumerate(raw_str_input):
  encoded_str += cipher_dict[char]

print(f'''\nHere is your encoded string: {encoded_str}''')
