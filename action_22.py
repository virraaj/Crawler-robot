'''
____________________________________________________________________________
*** Here latest version of playAction is defined. ***
* playAction method plays the given action by moving appropriate arms
(i.e up, down, left or right) in the given state. *
--> inputs are action = action that needs to be performed
               raw = current raw (position of second motor)
               col = current col (position of first motor)
               n =  Nos of total raws / cols
               p,p1 = handle for first and second motors respectively
--> defined new variable tDelay that controls and can change speed of the motors during the actions.
______________________________________________________________________________
'''


# ___________ impoering dependencies ___________ #

import time


# ___________ frange definition ___________ #

def frange(start, end, n):
    tmp = start
    step = (end - start) / (n-1)
    for i in range(0, n):
        yield tmp
        tmp += step


# ___________ playAction definition ___________ #

def playAction(action, raw, col, n, p, p1):
    '''
****************************************************************************
    values of action can be from [0,1,2,3]=[up,down,left,right]
    raw and col can be from range(0, n-1)
    and n = Nos. of steps we want
*****************************************************************************
    '''
    tDelay = 0.0065  # delay to control motor speeds
    positions = []  # positions of motor 1
    # define related pwm input values for all positions of first motor in a list
    for i in frange(3.0, 6.3, n):  # range of first motor
        positions.append(i)

    motor1_range = positions   # down to up
    # define related pwm input values for all positions of second motor in a list
    positionraw = []  # positions motor2
    for j in frange(8.5, 3.5, n):  # range of second motor
        positionraw.append(j)
    motor2_range = positionraw  # towards Right

    # performig required action.

    if action == 0 and raw > 0:  # up
        d = motor1_range[raw-1]
        c = motor1_range[raw]
        m = (motor1_range[raw-1]-motor1_range[raw])/25
        for x in range(0, 25):
            d = m*x+c
            p.ChangeDutyCycle(d)
            time.sleep(tDelay)
    elif action == 0 and raw <= 0:  # if already in top most raw
        print"UP motion not allowed"
    elif action == 1 and raw < n-1:  # down
        d = motor1_range[raw+1]
        c = motor1_range[raw]
        m = (motor1_range[raw+1]-motor1_range[raw])/25
        for x in range(0, 25):
            d = m*x+c
            p.ChangeDutyCycle(d)
            time.sleep(tDelay)
    elif action == 1 and raw >= n-1:  # if already in down most raw
        print"DOWN motion not allowed"
    elif action == 2 and col > 0:  # Left
        d = motor2_range[col-1]
        c = motor2_range[col]
        m = (motor2_range[col-1]-motor2_range[col])/25
        for x in range(0, 25):
            d = m*x+c
            p1.ChangeDutyCycle(d)
            time.sleep(tDelay)
    elif action == 2 and col <= 0:  # if already in left most col
        print"Left motion not allowed"
    elif action == 3 and col < n-1:  # Right
        d = motor2_range[col+1]
        c = motor2_range[col]
        m = (motor2_range[col+1]-motor2_range[col])/25
        for x in range(0, 25):
            d = m*x+c
            p1.ChangeDutyCycle(d)
            time.sleep(tDelay)
    elif action == 3 and col >= n-1:  # if already in right most col
        print"Right motion not allowed"
