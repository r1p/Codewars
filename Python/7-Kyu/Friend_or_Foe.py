'''
Description:
Make a program that filters a list of strings and returns a list with only your friends name in it.
If a name has exactly 4 letters in it, you can be sure that it has to be a friend of yours! Otherwise, you can be sure he's not...
Ex: Input = ["Ryan", "Kieran", "Jason", "Yous"], Output = ["Ryan", "Yous"]
i.e.
friend ["Ryan", "Kieran", "Mark"] `shouldBe` ["Ryan", "Mark"]
Note: keep the original order of the names in the output.

Categories:
#Fundamentals

Solve date:
20 Jul 2021 
'''

def friend(friends:list) -> list:
    real_friends = []

    for friend in friends:
        real_friends.append(friend) if len(friend) == 4 else 0
        
    return real_friends
