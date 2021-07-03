
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

key_errors = []
for x in range(100, 999):
  try:
    hundreds_digit = x // 100
    tens_digit = x // 10 - hundreds_digit * 10
    ones_digit = x % 10

    print_str = f'{ones_dict[hundreds_digit]} hundred'
    if tens_digit == 0 and ones_digit > 0:
      print_str += ' and '

    if tens_digit >= 2:
      print_str += f' {tens_dict[tens_digit]}'

    if tens_digit >= 2 and ones_digit > 0:
      print_str += '-'

    if ones_digit > 0 and tens_digit != 1:
      print_str += f'{ones_dict[ones_digit]}'

    if tens_digit == 1 and ones_digit > 0:
      print_str += f' and {teens_dict[ones_digit]}'
    elif tens_digit == 1 and ones_digit == 0:
      print_str += ' ten'

    print(hundreds_digit, tens_digit, ones_digit)

    print(print_str)

  except KeyError:
    key_errors.append(x)
print(key_errors)
