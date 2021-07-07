tens_dict = {
  2: 'twenty',
  3: 'thirty',
  4: 'forty',
  5: 'fifty',
  6: 'sixty',
  7: 'seventy',
  8: 'eighty',
  9: 'ninety'
}

ones_dict = {
  1: 'one',
  2: 'two',
  3: 'three',
  4: 'four',
  5: 'five',
  6: 'six',
  7: 'seven',
  8: 'eight',
  9: 'nine',
}

# x = 32

# run this code then comment this block out
# for x in range(100):
#   tens_digit = x // 10
#   ones_digit = x % 10

#   print(f'{tens_dict[tens_digit]}-{ones_dict[ones_digit]}')


# then comment this block in, and run it again
key_errors = []
for x in range(100):
  try:
    tens_digit = x // 10
    ones_digit = x % 10

    print(f'{tens_dict[tens_digit]}-{ones_dict[ones_digit]}')
  except KeyError:
    key_errors.append(x)

print(key_errors)