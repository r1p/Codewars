'''
Description:
Return the number (count) of vowels in the given string.
We will consider a, e, i, o, u as vowels for this Kata (but not y).
The input string will only consist of lower case letters and/or spaces.

Categories:
#Debugging #Fundamentals

Solve date:
07 Feb 2022 
'''

def get_count(sentence):
    count = 0
    vowels = {"a", "e", "i", "o", "u"}
    for x in sentence:
        if x in vowels:
            count += 1
    return count
