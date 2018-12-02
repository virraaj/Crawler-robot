'''
____________________________________________________________________________
* generate_rewardmatri() generates an empty reward matrix depending on the size
of state space (Nos of cols and raws)
it takes size total nos of raw or col as an input. *
______________________________________________________________________________
'''

# ___________ impoering dependencies ___________ #

from copy import deepcopy


# ___________ method definition ___________ #

def generate_rewardmatrix(n):
    temp = []
    reward = []
    for i in range(0, n):
        temp.append({})
    for i in range(0, n):
        reward.append(deepcopy(temp))

    for raw in range(0, n):
        for col in range(0, n):
            if raw == 0:
                reward[raw][col][0] = None  # up motion not allowed
                reward[raw][col][1] = 0  # down motion
                if col == 0:
                    reward[raw][col][2] = None  # left motion not allowed
                    reward[raw][col][3] = 0  # right motion
                elif col == n-1:
                    reward[raw][col][2] = 0  # left motion
                    reward[raw][col][3] = None  # right motion not allowed
                else:
                    reward[raw][col][2] = 0  # left motion
                    reward[raw][col][3] = 0  # right mption
            elif raw == n-1:
                reward[raw][col][1] = None  # down motion not allowed
                reward[raw][col][0] = 0  # up motion
                if col == 0:
                    reward[raw][col][2] = None  # left motion not allowed
                    reward[raw][col][3] = 0  # right motion
                elif col == n-1:
                    reward[raw][col][2] = 0  # left motion
                    reward[raw][col][3] = None  # right motion not allowed
                else:
                    reward[raw][col][2] = 0  # left motion
                    reward[raw][col][3] = 0  # right mption
            else:
                reward[raw][col][0] = 0  # up motion
                reward[raw][col][1] = 0  # down motion
                if col == 0:
                    reward[raw][col][2] = None  # left motion not allowed
                    reward[raw][col][3] = 0  # right motion
                elif col == n-1:
                    reward[raw][col][2] = 0  # left motion
                    reward[raw][col][3] = None  # right motion not allowed
                else:
                    reward[raw][col][2] = 0  # left motion
                    reward[raw][col][3] = 0  # right mption
    return reward
