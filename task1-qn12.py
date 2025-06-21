'Write a function to check if a string is a palindrome without using slicing or Python built-ins that reverse strings.'

def palindrome(s):
    for i in range(len(s) // 2):
        if s[i] != s[len(s) - 1 - i]:
            return False
    return True

word = input("Enter a word: ")

if palindrome(word):
    print("It's a palindrome!")
else:
    print("Not a palindrome.")