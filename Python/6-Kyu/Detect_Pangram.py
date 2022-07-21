'''
Description:
A pangram is a sentence that contains every single letter of the alphabet at least once. For example, the sentence "The quick brown fox jumps over the lazy dog" is a pangram, because it uses the letters A-Z at least once (case is irrelevant).
Given a string, detect whether or not it is a pangram. Return True if it is, False if not. Ignore numbers and punctuation.

Categories:
#Strings #DataStructures #Fundamentals

Solve date:
21 Jul 2021 
'''


import string

def is_pangram(s):
    string_2 = ""
    for letter in s:
        if letter.isalpha():
            string_2 += letter

    # Convert to lower case, remove duped letters, and sort alphabetically:
    string_3 = sorted(list(dict.fromkeys(list(string_2.lower()))))

    if len(string_3) < 26:
        return False
    return True
