def reverse_words(text):
    
    text.split()
    output = []

    for x in text[::-1]:
       
       output.append(x)

    # output = output.reversed()
    output_1 = []
    for y in output[::-1]:
        output_1.append(y)
    output_ = " ".join(output)
    return output_1
  

print(reverse_words('The quick brown fox jumps over the lazy dog.'))