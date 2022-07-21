'''
Description:
Your task is to make a function that can take any non-negative integer as an argument and return it with its digits in descending order. Essentially, rearrange the digits to create the highest possible number.

Categories:
#Fundamentals

Examples:
Input: 42145 Output: 54421
Input: 145263 Output: 654321
Input: 123456789 Output: 987654321

Solve date:
20 Jul 2021 
'''

def descending_order(num: int) -> int:
    list_num = [int(n) for n in str(num)]
    list_num.sort(reverse=True)
    list_number = [str(i) for i in list_num]
    number = "".join(list_number)
    return int(number)
