
#Cite: http://econowmics.com/python-rot-13-encryption-method/
# Rot 13
import string

# The alphabet

english_alphabet = string.ascii_lowercase

# Function to encrypt a text based on the Rot-13 method
def encrypt(text):
    """The function receives a string as input, and encrypts it using the Rot-13 method """
    
    # Transform the string to lower-case chars
    text = text.lower()
    
    # the encrypted message
    rot_13_message = ''
    
    # Replace each letter in the string with a letter which is 13 positions further
    for character in text:
        if character.isalpha:
            rot_13_message += english_alphabet[(english_alphabet.index(character) + 13) % 26]
        else:
            rot_13_message += character
    return rot_13_message

print(encrypt(input(" "))) 
  
