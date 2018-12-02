'''
____________________________________________________________________________
*** Returns list of empty value matrix and action matrix of given size here'n'. ***
* value matrix is filled with all zeros. *
* action matrix is filled with all 'None'. *
______________________________________________________________________________
'''


def initvalact(n):

    value = [[0]*n for i in range(n)]
    action = [[None]*n for i in range(n)]

    return value, action
