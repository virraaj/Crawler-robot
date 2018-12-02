'''
____________________________________________________________________________
*** It takes nos of raw or col and returns a symatric (raw = col) Q matrix.  ***
______________________________________________________________________________
'''


# ___________ impoering dependencies ___________ #

from copy import deepcopy


def qinitial(n):
    a = [0, 0, 0, 0]
    temp = []
    value = []
    for i in range(1, n+1):
        temp.append(deepcopy(a))
    for j in range(1, n+1):
        value.append(deepcopy(temp))
    return value
