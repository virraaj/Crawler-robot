# import RPi.GPIO as GPIO
import time
# import pinSetup
# import gotopos
# import ipdb


def frange(start, end, n):
    # step = round(step,3)
    tmp = start
    step = (end - start) / (n-1)
    for i in range(0, n):
        yield tmp
        tmp += step


def playAction(action, raw, col, n, p, p1):
    '''
****************************************************************************
    values of a can be from [0,1,2,3]=[up,down,left,right]
    raw and col can be from range(0, n-1)
    and n = Nos. of steps we want
*****************************************************************************
    '''
    positions = []  # positions of motor 1
    for i in frange(2.5, 5.0, n):
        positions.append(round(i, 2))

    motor1_range = positions   # down to up
    # a1 = round(a1,2)
    print "1st_Motor_Range", motor1_range

    positionraw = []  # positions motor2
    for j in frange(3.0, 10.0, n):
        positionraw.append(round(j, 2))
    motor2_range = positionraw  # towards Right
    print "2nd_Mtor_Range=", motor2_range

    if action == 0 and raw > 0:  # up
        d = motor1_range[raw-1]
        print "d=", d
        p.ChangeDutyCycle(d)
        time.sleep(0.1)
    elif action == 0 and raw <= 0:
        print"UP motion not allowed"
    elif action == 1 and raw < n-1:  # down
        d = motor1_range[raw+1]
        print "d=", d
        p.ChangeDutyCycle(d)
        time.sleep(0.1)
    elif action == 1 and raw >= n-1:
        print"DOWN motion not allowed"
    elif action == 2 and col > 0:  # Left
        d = motor2_range[col-1]
        p1.ChangeDutyCycle(d)
        time.sleep(0.1)
    elif action == 2 and col <= 0:
        print"Left motion not allowed"
    elif action == 3 and col < n-1:  # Right
        d = motor2_range[col+1]
        p1.ChangeDutyCycle(d)
        time.sleep(0.1)
    elif action == 3 and col >= n-1:
        print"Right motion not allowed"


'''
******************************************************************************
just for a temporary testing following code
******************************************************************************
pinVar = pinSetup.pinSetup()
p = pinVar[0]
p1 = pinVar[1]
encoder = pinVar[2]
ENClast = pinVar[3]
p.start(4.0)
p1.start(6.5)
gotopos.gotopos(2,2,p,p1)
time.sleep(2.0)
playAction(3, 2, 2, 5)
'''
