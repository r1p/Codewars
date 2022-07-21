'''
Description:
Write a function that takes in a string of one or more words, and returns the same string, but with all five or more letter words reversed (Just like the name of this Kata). Strings passed in will consist of only letters and spaces. Spaces will be included only when more than one word is present.

Examples:
spinWords( "Hey fellow warriors" ) => returns "Hey wollef sroirraw"
spinWords( "This is a test") => returns "This is a test"
spinWords( "This is another test" )=> returns "This is rehtona test"

Categories:
#Strings #Algorithms

Solve date:
09 Feb 2022 
'''

def spin_words(sentence):
    ret = [word if len(word) < 5 else word[::-1] for word in sentence.split()]
    return(" ".join(ret))
