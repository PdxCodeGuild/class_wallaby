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
teens_dict = {
  0: 'ten',
  1: 'eleven',
  2: 'twelve',
  3: 'thirteen',
  4: 'fourteen',
  5: 'fifteen',
  6: 'sixteen',
  7: 'seventeen',
  8: 'eighteeen',
  9: 'nineteen'
}
ones_dict = {
  0: '',
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

# for x in range(99):
#   output_str = ''
#   tens_digit = x // 10
#   ones_digit = x % 10

#   if tens_digit >= 2:
#     output_str += tens_dict[tens_digit]

#   elif tens_digit == 1:
#     output_str += teens_dict[ones_digit]

#   if tens_digit != 1:
#     output_str += ones_dict[ones_digit]
#   print(output_str)


# then comment this block in, and run it again
key_errors = []
for x in range(99):
  try:
    output_str = ''
    tens_digit = x // 10
    ones_digit = x % 10

    if tens_digit >= 2:
      output_str += tens_dict[tens_digit]

    elif tens_digit == 1:
      output_str += teens_dict[ones_digit]

    if tens_digit != 1:
      output_str += ones_dict[ones_digit]
    print(output_str)

  except KeyError:
    key_errors.append(x)
print(key_errors)

