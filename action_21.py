# import RPi.GPIO as GPIO
# import time
import pinSetup


def frange(start, end, n):
    # step = round(step,3)
    tmp = start
    step = (end - start) / (n-1)
    for i in range(0, n):
        yield tmp
        tmp += step


def playAction(a, s1, s2, n):
    '''
****************************************************************************
    values of a can be from [0,1,2,3]=[up,down,left,right]
    s1 and s2 can be from range(0, n-1)
    and n = Nos. of steps we want
*****************************************************************************
    '''
    positions = []  # positions of motor 1
    for i in frange(5.0, 3.0, n):
        positions.append(round(i, 2))

    motor1_range = positions   # down to up
    # a1 = round(a1,2)
    print "1st_Motor_Range", motor1_range

    positions1 = []  # positions motor2
    for j in frange(10.0, 3.0, n):
        positions1.append(round(j, 2))
    motor2_range = positions1  # towards Right
    print "2nd_Mtor_Range=", motor2_range

    if a == 0 and s1 > 0:  # up
        # p.start(2.5)  # Initialising up down motor
        d = motor1_range[s1-1]
        print "d=", d
        p.ChangeDutyCycle(d)
    #    time.sleep(0.5)
    elif a == 0 and s1 <= 0:
        print"UP motion not allowed"
    elif a == 1 and s1 < n-1:  # down
        #    p.start(2.5)
        d = motor1_range[s1+1]
        print "d=", d
        p.ChangeDutyCycle(d)
    #    time.sleep(0.5)
    elif a == 1 and s1 >= n-1:
        print"DOWN motion not allowed"
    elif a == 2 and s2 > 0:  # Left
        # p1.start(2.5)
        d = motor2_range[s2-1]
        p1.ChangeDutyCycle(d)
        # time.sleep(0.5)
    elif a == 2 and s2 <= 0:
        print"Left motion not allowed"
    elif a == 3 and s2 < n-1:  # Right
        # p1.start(2.5)
        d = motor2_range[s2+1]
        p1.ChangeDutyCycle(d)
        # time.sleep(0.5)
    elif a == 3 and s2 >= n-1:
        print"Right motion not allowed"


pinVar = pinSetup()
p = pinVar(0)
p1 = pinVar(1)
encoder = pinVar(2)
ENClast = pinVar(3)
playAction(3, 5.0, 10.0, 4)
