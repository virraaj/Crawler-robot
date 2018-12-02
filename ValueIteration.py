'''
____________________________________________________________________________
* ValueIteration takes value matrix and reward matrix as input to compute policy.*
it returtns a list of value matrix and policy learned.
* For actions always remember notations:
0 = up ; 1 = down ; 2 = left ; 3= right. *
* generateDummy generating Dummy value vector with norm = 1 to apply condition
error between vlast and v*
* error returns sum of squared error between given two lists*
______________________________________________________________________________
'''


# ___________ impoering dependencies ___________ #


import numpy as np
from copy import deepcopy
from Error import error
from Dummy import generateDummy
gama = 0.9  # discount factor


# ___________ valueitaration method definition ___________ #

def valueiteration(v, reward, a):
    # vlast will be used to memorize values in v matrix during previous iteration
    vlast = generateDummy(v)
    print (error(v, vlast))  # print initial error betwwen v and vlast.
    while error(v, vlast) >= 10**(-5):  # thresold value for convergence
        vlast = deepcopy(v)  # copying current V in Vlast
        m = np.shape(v)  # size of value matrix
        for i in range(0, m[0]):  # Nos. of Raws
            for j in range(0, m[1]):  # Nos. of Columns
                for k in range(0, 4):  # Nos. of actions
                    if k == 0 and i > 0:  # Upper movement for all Raws -1st Raw
                        temp0 = reward[i][j][k] + gama * v[i-1][j]
                    elif k == 0 and i == 0:  # Upper movement for 1st Raw (All Cols)
                        temp0 = None
                    if k == 1 and i < m[0]-1:  # Down movement for all raws - last Raw
                        temp1 = reward[i][j][k] + gama * v[i+1][j]
                    elif k == 1 and i == m[0]-1:  # Down movement for last Raw(All Cols)
                        temp1 = None
                    if k == 2 and j > 0:  # Left movement for all Cols - 1st  Cols
                        temp2 = reward[i][j][k] + gama * v[i][j-1]
                    elif k == 2 and j == 0:  # Left movement for 1st Cols(all raws)
                        temp2 = None
                    if k == 3 and j < m[1]-1:  # Right movement for all Cols - last  Cols
                        temp3 = reward[i][j][k] + gama * v[i][j+1]
                    elif k == 3 and j == m[1]-1:  # Right movement for last Cols(all raws)
                        temp3 = None
                v[i][j] = max(temp0, temp1, temp2, temp3)  # taking max of all actions

                # a stores which action is taken to get the value (ultimate policy)
                if v[i][j] == temp0:
                    a[i][j] = 0
                if v[i][j] == temp1:
                    a[i][j] = 1
                if v[i][j] == temp2:
                    a[i][j] = 2
                if v[i][j] == temp3:
                    a[i][j] = 3
                if v[i][j] == None:
                    v[i][j] = 0
    return v, a
