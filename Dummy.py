'''
____________________________________________________________________________
* generateDummy generating Dummy value vector with norm = 1 to apply condition
error between vlast and v. *
* generateDummy method generates dummy list of same size with first element 1. *
______________________________________________________________________________
'''


# ___________ impoering dependencies ___________ #

import numpy as np


# ___________ method definition ___________ #

def generateDummy(v1):
    s = np.shape(v1)
    layer = len(s)
    List = []
    appendElement = 1
    cnt = 0
    for lyr in range(0, layer):
        cnt += 1
        List = []
        for ele in range(0, s[(layer-1) - lyr]):
            List.append(appendElement)
            if cnt == 1:
                appendElement = 0
        appendElement = List

    return List
