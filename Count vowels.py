#Question  6: Count Vowels

def count_vowels(text):
    vowels ="aeiouAEIOU"
    vowel_count = 0
    for char in text:
        if char .isalpha() and char in vowels:
             vowel_count += 1
    return vowel_count

print(count_vowels("Hello world"))