# 1. Remove all vowel characters from a string.
def remove_vowels(s):
    vowels = "aeiouAEIOU"
    return ''.join(char for char in s if char not in vowels)
print(remove_vowels("hello world"))