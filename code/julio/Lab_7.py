def rot13(txt):
    """Applies the rot13 cipher to a text. 
    In the case of a plain text this will result in a cipher text
    being preoduced. Ad a cipher text will be deciphered.
    
    args: txt : a text on which rot13 will be applied
    returns: encrypted/decrypted version of the text"""

    result = []
    for letter in txt:
        value = ord(letter)
        if value >= ord('A') and value <= ord('Z'):
            value += 13
            if value > ord('Z'):
                value = (value - ord('Z')) + ord('A') - 1
                
    
        elif value >= ord('a') and value <= ord('z'):
            value += 13
            if value > ord('z'):
                value = (value - ord('z')) + ord('a') - 1

        result.append( chr(value) )

    return "".join(result)


while True:
    msg = input("please type a message to encrypt or decrypt").strip()
    if not msg:
        break
    enc = rot13(msg)
    print(enc)
    print(rot13(enc))