import string

abc = string.ascii_lowercase
print(abc)
user = input("Welcome ! please enter a word to be encrypted : ")
dict = {}
all = ''

for i, char in enumerate(abc):
  dict[char] = abc[(i + 13) % 26]

for i, char in enumerate(user):
  all += dict[char]

print(f"ROT13 code: {all}")