#Description: Write a function named count_vowels that
# takes a string as an argument and return
# the count of vowels (a, e, i, o, u) in the string.
#The function should be case-insensitive, counting both uppercase and lowercase vowels.

def count_vowels(word):
    vowels = "aeiou"
    return sum(1 for char in word.lower() if char in vowels)

word = "Hello, World!"
print("Number of vowels:", count_vowels(word))  # Output: Number of vowels: 3
