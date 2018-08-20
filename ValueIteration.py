# let's start with 3x3 matrix for valueiteration
# always use the rewards as dictionary of up, down, left, right.
import numpy as np
import ipdb
from copy import deepcopy
from Error import error
gama = 0.9  # discount factor assuming to be 0.9
# reward vector is as below
# 0 = up / 1 = down / 2 = left / 3= right
'''
reward = [[{0: None, 1: 0, 2: None, 3: 0},  # state = 1
           {0: None, 1: 0, 2: 0, 3: 0},  # State = 2
           {0: None, 1: 0, 2: 0, 3: None}],  # State = 3
          [{0: 0, 1: 0, 2: None, 3: 0},  # State = 4
           {0: 0, 1: 0, 2: 0, 3: 0},  # State = 5
           {0: 0, 1: 0, 2: 0, 3: None}],  # State = 6
          [{0: 0, 1: None, 2: None, 3: -1},  # State = 7
           {0: 0, 1: None, 2: 1, 3: -1},  # State = 8
           {0: 0, 1: None, 2: 1, 3: None}]]  # State = 9
'''
reward = [{0: None, 1: 0, 2: None, 3: 0}, {0: None, 1: 0, 2: 0, 3: 0}, {0: None, 1: 0, 2: 0, 3: None}]
         [{0: 0, 1: 1, 2: None, 3: 0}, {0: 0, 1: 1, 2: 0, 3: 0}, {0: 0, 1: 0, 2: 0, 3: None}]
         [{0: 0, 1: None, 2: None, 3: -1}, {0: 0, 1: None, 2: 1, 3: -1}, {0: 0, 1: None, 2: 0, 3: None}]
v = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]  # initial value vector


def valueiteration(v, reward):
    a = [[None, None, None], [None, None, None],  [None, None, None]]
    # initializing a dummy last value matrix  to enter Error loop
    vlast = [[1, 0, 0], [0, 0, 0], [0, 0, 0]]
    print (error(v, vlast))
    while error(v, vlast) >= 10**(-3):
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
                # a stores which action is taken to get the value
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
        # ipdb.set_trace()
    return v, a


trial = valueiteration(v, reward)
print(trial[0])
print("\n")
print(trial[1])
