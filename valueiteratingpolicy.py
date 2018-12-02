'''
____________________________________________________________________________
*** Valueiterating policy combines all programs and functions togather to make
crawler work on VALUEITERATION. ***
* rewardsegregation takes State matrix size and collects all rewards by
performing all actions possible in each states. *
* ValueIteration takes value matrix and reward matrix as input to compute policy.*
* playAction method plays the given action by moving appropriate arms
(i.e up, down, left or right) in the given state. *
* pinSetup() is a method that single handedly defines all the required input and
output pins of the RaspberryPi Zero board. *
______________________________________________________________________________
'''

# ___________ impoering dependencies ___________ #

import ValueIteration
import pinSetup
import action_22 as act
import gotopos
import initvalact
import rewardsegregation_20 as rewardsegregation

# ___________ main function definition ___________ #
# takes 'n = Nos of columns and Nos of raws' as input arguement


def valueiteratingpolicy(n, p, p1, encoder, ENClast):
    v = initvalact.initvalact(n)
    # returns list of empty value matrix and action matrix of given size here'n'
    value = v[0]  # assigning empty value matrix
    action = v[1]  # assigning empty action matrix
    reward = rewardsegregation.rewardsegregation(n, p, p1, encoder, ENClast)
    # callling reward segrigation to collect rewards by performing all actions
    print reward  # print collected rewards matrix
    test = ValueIteration.valueiteration(value, reward, action)
    # valueiteration is a function where all computation takes place for according to value iteration algorithm and returns a learned policy
    policy = test[1]  # assigning collected policy
    print policy
    raw = 0  # initializing variable raw
    col = 0  # initializing variable col
    gotopos.gotopos(raw, col, p, p1, n)  # bring both arms in home initial position
    # 0 = up / 1 = down / 2 = left / 3= right
    global val1
    val1 = pinSetup.valueRead_ON()  # read ON/OFF switch
    while True and val1 == 0:  # checks for poition of ON/OFF switch
        # here we check for policy for current raw col state and performing action plus updating raw and col values accordingly
        if action[raw][col] == 0:  # up action
            act.playAction(0, raw, col, n, p, p1)  # perform action
            raw = raw - 1

        elif action[raw][col] == 1:  # down action
            act.playAction(1, raw, col, n, p, p1)  # perform action
            raw = raw + 1

        elif action[raw][col] == 2:  # left action
            act.playAction(2, raw, col, n, p, p1)  # perform action
            col = col - 1

        elif action[raw][col] == 3:  # right action
            act.playAction(3, raw, col, n, p, p1)  # perform action
            col = col + 1
        val1 = pinSetup.valueRead_ON()  # updating ON/OFF switch state
    if val1 == 1:  # if switch is at OFF position
        print "Stop"
