import string

alphabet = string.ascii_lowercase

user_str = input("Type a secret message for ROT13 encryption: ")

def encryption(message):
    """For each character, 
    find the corresponding character, 
    add it to an output string."""
    output = ''
    for letter in message:
        output += alphabet[(alphabet.index(letter)+ 13) % 26]
    return output

print(f"Encrypted ROT13 message: {encryption(user_str)}")

# how to deal with spaces?

# test: 'help me' = 'uryc zr'