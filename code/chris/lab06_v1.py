card1 = '4556737586899855'

# *** F U N C T I O N S ***
def is_valid_credit_card(card_num_str):
  chars_list = list(card_num_str)
  ints_list = []
  for char in chars_list:
    ints_list.append(int(char))
  last_digit = ints_list.pop(-1)

  reversed_list = []
  while len(ints_list) > 0:
    reversed_list.append(ints_list.pop(len(ints_list) - 1))

  for idx in range(len(reversed_list)):
    if idx % 2 == 0:
      reversed_list[idx] = reversed_list[idx] * 2

  for idx in range(len(reversed_list)):
    if reversed_list[idx] > 9:
      reversed_list[idx] -= 9

  sum = 0
  for num in reversed_list:
    sum += num

  second_digit_of_sum = int(str(sum)[1])

  if second_digit_of_sum == last_digit:
    return True
  else:
    return False


print(is_valid_credit_card(card1))

# *** T E S T S ***