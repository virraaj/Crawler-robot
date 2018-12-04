'''
____________________________________________________________________________
*** Q(λ)-learning implements Peng's Q(λ)-learning method and algorithm. ***
* epsilon_greedy_policy() takes list of actions possible, epsilon value and best
action and returns list of probablities of selecting a action in next step with
epsilon greedy policy *
* action_select() takes current position (state) as raw and col number and
returns all possible actions in that perticular position. *
* generateDummy() generating Dummy value vector with norm = 1 to apply condition
error between Qlast and Q*
* qError() returns sum of squared error between given two lists*
* playAction() method plays the given action by moving appropriate arms
(i.e up, down, left or right) in the given state. *
* pinSetup() is a method that single handedly defines all the required input and
output pins of the RaspberryPi Zero board. *
--> in V3.1 restriction for reward controlling is applied successfully
--> for actions consider following notation:
        0 = up ; 1 = down ; 2 = left ; 3= right
______________________________________________________________________________
'''


# ___________ impoering dependencies ___________ #

import numpy as np
import time
from Error import qError
import random
from Dummy import generateDummy
from copy import deepcopy
import pinSetup
import action_22 as act
import generate_rewardmatrix
import gotopos
import initvalact
import qinitial

# ___________ learning parameters ___________ #

epsilon = 0.7  # initilization for epsilon greedy policy
bita = 1/2   # bita definition
lamda = 1/2  # λ value for q(λ) learning
gama = 0.7  # discount factor assuming to be 0.9


# ___________ method definition ___________ #

def epsilon_greedy_policy(Q, actions, epsilon):
    '''
    Create a policy in which epsilon dictates how likely it will
    take a random action.

    :param q: Q values of the perticular state
    :param nA: number of actions (int)
    :param epsilon: chance it will take a random move (float)
    :return: probability of each action to be taken (list)
    '''
    q = []
    maxind = []
    temp = 0
    for action in actions:
        q.append(Q[action])
    nA = len(actions)
    maxval = max(q)
    for temp in range(len(q)):
        if maxval == q[temp]:
            maxind.append(temp)
    if len(maxind) == 1:
        probs = np.ones(nA) * epsilon / nA
        best_action = np.argmax(q)
        probs[best_action] += 1.0 - epsilon
    else:
        probs = np.ones(nA) * epsilon / nA
        for temp in range(len(q)):
            if temp in maxind:
                probs[temp] += (1.0 - epsilon)/len(maxind)
    return probs


# ___________ method definition ___________ #

def action_select(raw, col, n):
    # action selection according to selction of state
    if raw == 0 and col == 0:
        return [1, 3]
    elif raw == 0 and (col == -1 or col == n-1):
        return [1, 2]
    elif raw == 0:
        return [1, 2, 3]

    elif raw == n-1 and col == 0:
        return [0, 3]
    elif raw == n-1 and (col == -1 or col == n-1):
        return [0, 2]
    elif raw == n-1:
        return [0, 2, 3]

    elif col == 0:
        return [0, 1, 3]
    elif (col == -1 or col == n-1):
        return [0, 1, 2]

    else:
        return [0, 1, 2, 3]  # cells where all four actions are possible


# ___________ method definition ___________ #

def qLamda(n, p, p1, encoder, ENClast):
    v = initvalact.initvalact(n)  # initialization for action matrix
    Q = qinitial.qinitial(n)  # initialization for Q matrix
    # kMatrix keeps track of nos of time an state action pair repeats
    kMatrix = qinitial.qinitial(n)
    # initialization for TD(λ) performance
    Tr = qinitial.qinitial(n)
    a = v[1]  # action matrix assignment
    size = np.shape(Q)  # storing size of Q-matrix
    n = size[0]  # Nos of raws in Q matrix
    Qlast = generateDummy(Q)  # generating dummy of same sizq as Q to enter the while loop
    iteration = 0  # initializing the iteration
    reward = generate_rewardmatrix.generate_rewardmatrix(n)  # generating empty reward matrix
    # selecting random state for starting
    state = random.randint(1, size[0] * size[1])
    global val1
    val1 = pinSetup.valueRead_ON()  # position of ON/OFF switch
    while True and val1 == 0:  # check if switch is at ON position
        iteration += 1  # incresing iteration value
        Qlast = deepcopy(Q)  # copying Q to Qlast

        if iteration == 1:  # just for first iteration
            '''
            IN FOLLOWING STEP WE DEFINE RAW NUMBER DEPENDING ON RANDOMLY SELECTED 'state'.
            -> temp = to retrive raw and column from Nos of state generated by random selector
            -> state / Nos.of column will give us information about the raw number...
            -> for 3x4 (raw x column) state 1 to 4 are raw in 1 and state 5 to 8 are raw in 2
            -> for raw1(state 1 to 4)/4 (total columns) will be 0 < temp <= 1
            -> for raw1(state 5 to 8)/4 (total columns) will be 1 < temp <= 2
            '''
            temp = state / (size[1] * 1.0)  # defining a temporary variable
            direction = pinSetup.valueRead_dir()
            if ((temp).is_integer()):
                raw = int(temp) - 1
            else:
                raw = int(temp)

            '''
            IN FOLLOWING STEP WE DEFINE COL NUMBER DEPENDING ON RANDOMLY SELECTED 'state'.
            -> temp = modulo of state and Total column
            -> for column1(state 1,5,9) % 4 (total columns) will be 1 [i.e colum = 1-1 = 0]
            -> for column1(state 2,6,10) % 4 (total columns) will be 2 [i.e colum = 2-1 = 1]
            '''
            temp = state % size[1]
            col = temp - 1
            if col < 0:
                col = size[1] - 1
            else:
                pass
            gotopos.gotopos(raw, col, p, p1, n)  # to go to state that is selected randomly
            time.sleep(0.3)

        # updating epsilon values continiously depending on iteration number
        epsilon = (0.9/(np.exp(0.0005*(iteration**2-1))))+0.1
        # possible actions in current state
        possibleActions = action_select(raw, col, n)
        # computing probablity of each possible actions using epsilon greedy policy
        probablity = epsilon_greedy_policy(Q[raw][col], possibleActions, epsilon)
        # choosing action using probablity of action from previous step
        actionIndex = np.random.choice(len(probablity), p=probablity)
        action = possibleActions[actionIndex]

        '''
        ****************************************************************
                defining nextstate according to choosen action
        ****************************************************************
        '''
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
            nextstate = Q[raw][col+1]
            rawtemp = raw  # raw of nextstep
            coltemp = col + 1  # col of nextstep
        # try executing the Q-iteration formula with no errors..

        '''
        ****************************************************************
        performing action and collecting rewards and updating Q matrix
        ****************************************************************
        '''
        ENClast = encoder.getData()  # encoder reading before action
        act.playAction(action, raw, col, size[0], p, p1)  # performing action
        time.sleep(0.1)
        if action == 0 or action == 1:
            ENClast = encoder.getData()
        ENC = encoder.getData()  # encoder reading after action
        if direction != pinSetup.valueRead_dir():  # if direction switch is changed
            iteration = 2  # resetting iteration to 2 (controls epsilon value)
            kMatrix = qinitial.qinitial(n)  # resetting
            Tr = qinitial.qinitial(n)   # resetting

        print direction
        print pinSetup.valueRead_dir()
        print epsilon
        direction = pinSetup.valueRead_dir()  # reading direction switch
        diff = ENC - ENClast
        # stroring in temporarary variable to control faulty rewards
        diff_temp = ((-1)**direction)*diff
        oldreward = reward[raw][col][action]  # old reward value of same state action pair

        '''
        ****************************************************************
        checking if the reward is under going big difference or a
        direcion difference then it applies restriction and perform same
        action again and collect the  reward for the same action again.
        This approach has saved alot of faulty computation.
        (Just double checks before updating reward value)
        ***************************************************************
        '''
        if (oldreward != 0 and diff_temp == 0) or (np.sign(oldreward) != np.sign(diff_temp) and oldreward != 0):
            print ("!! restriction applied !!")
            gotopos.gotopos(raw, col, p, p1, n)
            time.sleep(0.3)
            ENClast = encoder.getData()
            act.playAction(action, raw, col, size[0], p, p1)
            time.sleep(0.1)
            if action == 0 or action == 1:
                ENClast = encoder.getData()
            ENC = encoder.getData()
            diff = ENC - ENClast

        reward[raw][col][action] = ((-1)**direction)*diff
        kMatrix[raw][col][action] = kMatrix[raw][col][action] + 1

        '''
        ****************************************************************
        updating Q matrix values according to Q(λ)-Learning algorithm.
        ****************************************************************
        '''
        try:
            alpha = 1/((kMatrix[raw][col][action])**bita)
            eComplement = reward[raw][col][action] + gama * max(nextstate) - Q[raw][col][action]
            e = reward[raw][col][action] + gama * max(nextstate) - max(Q[raw][col])
            for r in range(size[0]):
                for c in range(size[1]):
                    for actn in action_select(raw, col, n):
                        Tr[r][c][actn] = gama * lamda * Tr[r][c][actn]
                        Q[r][c][actn] = Q[r][c][actn] + alpha * Tr[r][c][actn] * e

            Q[raw][col][action] = Q[raw][col][action] + alpha * eComplement
            Tr[raw][col][action] += 1
        # tracking if there is a type error (i.e. datatype missmatch) or not in above equation
        except TypeError as e:
            print("TypeError")
        print possibleActions
        print probablity
        print "raw= ", raw, "col = ", col, "action = ", action
        # overwriting current state values by next state
        raw = rawtemp
        col = coltemp
        print "qerror is", qError(Q, Qlast)
        print "reward is", reward
        print "iteration = ", iteration
        val1 = pinSetup.valueRead_ON()  # updating switch position

    '''
    ****************************************************************************
                        END OF WHILE LOOP
    ****************************************************************************
    '''
    # getting the appropriate action back from the given calculated values of Q matrix
    '''
    ****************************************************************************
                        Computing final policy from Q values
    ***************************************************************************
    '''
    print Tr
    print Q
    for r in range(0, size[0]):
        for c in range(0, size[1]):
            possibleActions = action_select(r, c, n)
            tempList = []
            for i in possibleActions:
                tempList.append(Q[r][c][i])
            a[r][c] = possibleActions[tempList.index(max(tempList))]
    # function returns Q matrix, action matrix and nos of iteration
    return Q, a, iteration