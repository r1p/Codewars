'''
Description:
Welcome. In this kata, you are asked to square every digit of a number and concatenate them.
For example, if we run 9119 through the function, 811181 will come out, because 92 is 81 and 12 is 1.
Note: The function accepts an integer and returns an integer

Categories:
#Debugging #Fundamentals

Solve date:
07 Feb 2022 
'''

def square_digits(num):
    test = ""
    for x in str(num):
        test += str(int(x)**2)
    return int(test)
