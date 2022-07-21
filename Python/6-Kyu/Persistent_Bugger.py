'''
Description:
Write a function, persistence, that takes in a positive parameter num and returns its multiplicative persistence, which is the number of times you must multiply the digits in num until you reach a single digit.
For example (Input --> Output):
39 --> 3 (because 3*9 = 27, 2*7 = 14, 1*4 = 4 and 4 has only one digit)
999 --> 4 (because 9*9*9 = 729, 7*2*9 = 126, 1*2*6 = 12, and finally 1*2 = 2)
4 --> 0 (because 4 is already a one-digit number)

Categories:
#Fundamentals

Solve date:
20 Jul 2021 
'''

import sys
import numpy as np

def persistence(n: int) -> int:
    if len(str(n)) == 1:
        return 0

    result = n
    iter = 0

    while len(str(result)) != 1:
        list_n = [int(x) for x in str(result)]
        result = np.prod(list_n)
        iter += 1
    return iter
