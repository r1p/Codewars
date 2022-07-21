'''
Description:
Move the first letter of each word to the end of it, then add "ay" to the end of the word. Leave punctuation marks untouched.

Examples:
pig_it('Pig latin is cool') # igPay atinlay siay oolcay
pig_it('Hello world !')     # elloHay orldway !

Categories:
#RegularExpressions #Algorithms

Solve date:
21 Jul 2021 
'''

def pig_it(text:str) -> str:
    result = ""
    text_list = text.split()
    for x in text_list:
        if x.isalpha():
            result += x[1:]+x[0] + "ay " # Move the first to the last position and append "ay "
        else:
            result += x + " "
    return result[:-1] # Remove the last char
