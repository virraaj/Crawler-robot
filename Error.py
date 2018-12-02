'''
____________________________________________________________________________
* error returns sum of squared error between given two lists in R2 space. *
* qError returns sum of squared error between given two lists in R3 space. *
______________________________________________________________________________
'''

# ___________ impoering dependencies ___________ #

import numpy as np


# ___________ error function for value iteration ___________ #

def error(v1, v2):
    s1 = np.shape(v1)
    s2 = np.shape(v2)
    if s1 == s2:
        err = 0
        for r in range(0, s1[0]):
            for c in range(0, s1[1]):
                err = err + (v1[r][c] - v2[r][c]) ** 2
        return err


# ___________ error function for Q and  Q(λ)-Learning ___________ #

def qError(v1, v2):
    s1 = np.shape(v1)
    s2 = np.shape(v2)
    if s1 == s2:
        err = 0
        for r in range(0, s1[0]):
            for c in range(0, s1[1]):
                for a in range(0, s1[2]):
                    err = err + (v1[r][c][a] - v2[r][c][a]) ** 2
        return err
