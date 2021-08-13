def check_anagram(str1: str, str2: str):
  str1 = ''.join(sorted(str1.lower().replace(' ', '')))
  str2 = ''.join(sorted(str2.lower().replace(' ', '')))
  if len(str1) != len(str2):
    return False
  for idx, char in enumerate(str1):
    if char != str2[idx]:
      return False
  print(str1, str2)
  return True



check_anagram('anaGram', 'nag a ram')
check_anagram('dormitory', 'dirty room')
check_anagram('aaeezz', 'a e z z e b')