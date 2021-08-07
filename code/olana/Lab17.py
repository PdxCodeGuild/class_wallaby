#Palindrome
def check_palindrome(str):
    for i in range(0, int(len(str)/2)):
        if str[i] != str[len(str)-i-1]:
            return False
    return True
 
word = input("Enter word: ")
ans = check_palindrome(word)
 
if (ans):
    print("Yes")
else:
    print("No")

#Anagrams
def word_anagram_checker(str):
    letters =list(str)
    return letters

while True:
    entry_1 = input(f'enter the first word: ')
    entry_1.lower()
    entry_2 = input(f'enter the second word: ')
    entry_2.lower()

    if list(entry_1) == list(entry_2):
        print (f'{entry_1} and {entry_2} are anagrams')
    else:
        print (f'{entry_1} and {entry_2} are not anagrams')