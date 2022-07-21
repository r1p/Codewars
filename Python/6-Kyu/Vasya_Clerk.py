'''
Description:
The new "Avengers" movie has just been released! There are a lot of people at the cinema box office standing in a huge line. Each of them has a single 100, 50 or 25 dollars bill. A "Avengers" ticket costs 25 dollars.
Vasya is currently working as a clerk. He wants to sell a ticket to every single person in this line.
Can Vasya sell a ticket to each person and give the change if he initially has no money and sells the tickets strictly in the order people follow in the line?
Return YES, if Vasya can sell a ticket to each person and give the change. Otherwise return NO.

Categories:
#Fundamentals #Mathematics #Algorithms #Logic #Numbers #Games

Solve date:
20 Jul 2021 
'''

def tickets(people:list) -> bool:
    bill_25 = 0
    bill_50 = 0
    bill_100 = 0

    for x in people:
        if x == 25:
            bill_25 += 1

        elif x == 50:
            bill_50 += 1
            bill_25 -= 1

        elif x == 100 and bill_50 > 0:
            bill_50 -= 1
            bill_25 -= 1

        elif x == 100 and bill_50 == 0:
            bill_25 -= 3

        if bill_25 < 0 or bill_50 < 0:
            return "NO"
            
    return "YES"
