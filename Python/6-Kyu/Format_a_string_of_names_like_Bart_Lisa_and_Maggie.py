'''
Description:
Given: an array containing hashes of names
Return: a string formatted as a list of names separated by commas except for the last two names, which should be separated by an ampersand.

Example:
namelist([ {'name': 'Bart'}, {'name': 'Lisa'}, {'name': 'Maggie'} ])
# returns 'Bart, Lisa & Maggie'

namelist([ {'name': 'Bart'}, {'name': 'Lisa'} ])
# returns 'Bart & Lisa'

namelist([ {'name': 'Bart'} ])
# returns 'Bart'

namelist([])
# returns ''

Note: all the hashes are pre-validated and will only contain A-Z, a-z, '-' and '.'.

Categories:
#Fundamentals #Strings #Data Types #Formatting #Algorithms #Logic

Solve date:
20 Jul 20
'''

def namelist(names):
    ret = ''
    if(len(names) == 1):
        return names[0]['name']
    elif(len(names) == 2):
        ret = ret + names[0]['name'] + " & " + names[1]['name']
    elif(len(names) > 2):
        for x in range(0, len(names)-1):
            ret = ret + names[x]['name'] + ", "
        ret = ret[:-2] + " & " + names[len(names)-1]['name']
    return ret
