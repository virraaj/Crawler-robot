# import RPi.GPIO as GPIO
import time
import pinSetup
import gotopos
#import ipdb
def frange(start, end, n):
    # step = round(step,3)
    tmp = start
    step = (end - start) / (n-1)
    for i in range(0, n):
        yield tmp
        tmp += step


def playAction(a, s1, s2, n, p, p1):
    '''
****************************************************************************
    values of a can be from [0,1,2,3]=[up,down,left,right]
    s1 and s2 can be from range(0, n-1)
    and n = Nos. of steps we want
*****************************************************************************
    '''
    positions = []  # positions of motor 1
    for i in frange(3.0, 5.0, n):
        positions.append(round(i, 2))

    motor1_range = positions   # down to up
    # a1 = round(a1,2)
    print "1st_Motor_Range", motor1_range

    positions1 = []  # positions motor2
    for j in frange(3.0, 10.0, n):
        positions1.append(round(j, 2))
    motor2_range = positions1  # towards Right
    print "2nd_Mtor_Range=", motor2_range

    if a == 0 and s1 > 0:  # up
        d = motor1_range[s1-1]
        print "d=", d
        p.ChangeDutyCycle(d)
        time.sleep(2.0)
    elif a == 0 and s1 <= 0:
        print"UP motion not allowed"
    elif a == 1 and s1 < n-1:  # down
        d = motor1_range[s1+1]
        print "d=", d
        p.ChangeDutyCycle(d)
        time.sleep(0.5)
    elif a == 1 and s1 >= n-1:
        print"DOWN motion not allowed"
    elif a == 2 and s2 > 0:  # Left
        d = motor2_range[s2-1]
        p1.ChangeDutyCycle(d)
        time.sleep(0.5)
    elif a == 2 and s2 <= 0:
        print"Left motion not allowed"
    elif a == 3 and s2 < n-1:  # Right
        d = motor2_range[s2+1]
        p1.ChangeDutyCycle(d)
        time.sleep(0.5)
    elif a == 3 and s2 >= n-1:
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
