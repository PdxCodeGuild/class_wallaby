import string
raw_str = input('\nEnter string to be encoded: ')
encoded_str = ''
alphabet = string.ascii_lowercase
alphabet_list = [char for char in alphabet]
cipher_dict = {}

for i, char in enumerate(alphabet_list):
  cipher_dict[char] = alphabet_list[(i + 13) % 26]

for i, char in enumerate(raw_str):
  encoded_str += cipher_dict[char]

print(f'''\nHere is your encoded string: {encoded_str}''')
