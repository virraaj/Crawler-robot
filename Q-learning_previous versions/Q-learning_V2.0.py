# Implementation  of Q-learning
# again for 3x3 matrix is the starting point
import numpy as np
import ipdb
from Error import qError
import random
from Dummy import generateDummy
from copy import deepcopy
gama = 0.9  # discount factor assuming to be 0.9
# reward vector is as below
# 0 = up / 1 = down / 2 = left / 3= right
reward = [[{0: None, 1: 0, 2: None, 3: 0},  # state = 1
           {0: None, 1: 0, 2: 0, 3: 0},  # State = 2
           {0: None, 1: 0, 2: 0, 3: None}],  # State = 3
          [{0: 0, 1: 0, 2: None, 3: 0},  # State = 4
           {0: 0, 1: 0, 2: 0, 3: 0},  # State = 5
           {0: 0, 1: 0, 2: 0, 3: None}],  # State = 6
          [{0: 0, 1: None, 2: None, 3: -1},  # State = 7
           {0: 0, 1: None, 2: 1, 3: -1},  # State = 8
           {0: 0, 1: None, 2: 1, 3: None}]]  # State = 9
# Here Q function is also function of state and actions
# Q is definded as matrix of 9 members.. every member is a state..
# containing Q values for all four possible actions
Q = [[[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]],  # State1,State2, Stete3
     [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]],  # State4, State5, State6
     [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]]  # State7, State8, State9
# Every time we do down action from a state we will be in new state which is 3
# member after it. (i.e. from state1 to state4) [This is valid only for 3x3]
# Every time we do up action from a state we will be in new state which is 3
# member before it. (i.e. from state4 to state1) [This is valid only for 3x3]
# Every Right action will take us to state which is 1 member after it. [not valid for state3, state6, state9]
# Every Left action will take us to state which is 1 member before it. [not valid for state1, state4, state7]


def qLearning(Q, reward):
    a = [[None, None, None], [None, None, None],  [None, None, None]]  # initializing action matrix
    # size = reading size of the given Q matrix [Nos of raws, Nos. of col, Nos. of actions possible per state]
    size = np.shape(Q)  # storing size of Q-matrix
    Qlast = generateDummy(Q)  # generating dummy of same sizq as Q to enter the while loop
    iteration = 0  # initializing the iteration
    while qError(Q, Qlast) > 10**-3 or Q == Qlast:  # check for the error value to be 10**-3 or Q = Qlast
        # we want here Q!=Qlast becauses in starting phase if reward is zero in next step we will read error = 0
        # and this will cause us to fall out of the loop
        iteration += 1  # incresing iteration value
        Qlast = deepcopy(Q)  # copying Q to Qlast
        # state =  selecting state randomly every time depending on the Q size
        state = random.randint(1, size[0] * size[1])
        # temp = to retrive raw and column from Nos of state generated by random selector
        # state / Nos.of column will give us information about the raw number...
        # for 3x4 (raw x column) state 1 to 4 are raw in 1 and state 5 to 8 are raw in 2
        # for raw1(state 1 to 4)/4 (total columns) will be 0 < temp <= 1
        # for raw1(state 5 to 8)/4 (total columns) will be 1 < temp <= 2
        temp = state / (size[1] * 1.0)  # defining a temporary variable
        if ((temp).is_integer()):
            raw = int(temp) - 1
        else:
            raw = int(temp)
        # temp = modulo of state and Total column
        # for column1(state 1,5,9) % 4 (total columns) will be 1 [i.e colum = 1-1 = 0]
        # for column1(state 2,6,10) % 4 (total columns) will be 2 [i.e colum = 2-1 = 1]
        temp = state % size[1]
        col = temp - 1
        if col < 0:
            col = size[1] - 1
        else:
            pass
        # ipdb.set_trace()
        for i in range(0, 20):
            # action selection according to selction of state
            if raw == 0 and col == 0:
                action = random.choice([1, 3])
            elif raw == 0 and (col == -1 or col == size[1]-1):
                action = random.choice([1, 2])
            elif raw == 0:
                action = random.choice([1, 2, 3])

            elif raw == size[0]-1 and col == 0:
                action = random.choice([0, 3])
            elif raw == size[0]-1 and (col == -1 or col == size[1]-1):
                action = random.choice([0, 2])
            elif raw == size[0]-1:
                action = random.choice([0, 2, 3])

            elif col == 0:
                action = random.choice([0, 1, 3])
            elif (col == -1 or col == size[1]-1):
                action = random.choice([0, 1, 2])

            else:
                action = random.randint(0, 3)  # cells where all four actions are possible

            # defining nextstate according to choosen action
            if action == 0:  # Up movement
                nextstate = Q[raw-1][col]
                rawtemp = raw - 1  # raw of nextstep
                coltemp = col  # col of nextstep
            elif action == 1:  # Down movememt
                nextstate = Q[raw+1][col]
                rawtemp = raw + 1  # raw of nextstep
                coltemp = col  # col of nextstep
            elif action == 2:  # Left movement
                nextstate = Q[raw][col-1]
                rawtemp = raw  # raw of nextstep
                coltemp = col - 1  # col of nextstep
            else:  # Right movement
                # ipdb.set_trace()
                nextstate = Q[raw][col+1]
                rawtemp = raw  # raw of nextstep
                coltemp = col + 1  # col of nextstep
            # ipdb.set_trace()
            # try executing the Q-iteration formula with no errors..
            '''
            _____ADD HERE____
            ACTION_PERFORMANCE FUNCTION
            UPDATE_REWARD FUNCTION
            '''
            try:
                Q[raw][col][action] = reward[raw][col][action] + gama * (max(nextstate))
            # tracking if there is a type error (i.e. datatype missmatch) or not in above equation
            except TypeError as e:
                print("TypeError")
            raw = rawtemp
            col = coltemp

    # getting the appropriate action back from the given calculated values of Q matrix
    for r in range(0, size[0]):
        for c in range(0, size[1]):
            # ipdb.set_trace()
            a[r][c] = Q[r][c].index(max(Q[r][c]))
    # ipdb.set_trace()
    # function returns Q matrix, action matrix and nos of iteration
    return Q, a, iteration


# trial run of the function
trial = qLearning(Q, reward)
print(trial[0])
print("\n")
print(trial[1])
print("\n")
print(trial[2])
