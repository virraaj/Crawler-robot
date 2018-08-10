import RPi.GPIO as GPIO
import time


def frange(start, end, step):
    #step = round(step,3)
    tmp = start
    while(tmp >= end):
        yield tmp
        tmp -= step


def playAction(a, s1, s2):
    servoPIN = 17
    servoPIN1 = 4
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(servoPIN, GPIO.OUT)
    GPIO.setup(servoPIN1, GPIO.OUT)
    p = GPIO.PWM(servoPIN, 50)  # GPIO 17 als PWM mit 50Hz
    p1 = GPIO.PWM(servoPIN1, 50)
    n = 4
    # p.start(2.5) # Initialising inside the respective loops
    # p1.start(2.5)
    positions = []
    for i in frange(5.0, 3.0, (5-3.0)/(n-1)):
        positions.append(round(i, 2))

    up = positions   # down to up
    #a1 = round(a1,2)
    print "up=", up

    down = sorted(up)  # up to down
    print "down=", down
    positions1 = []
    for j in frange(10.0, 3.0, round((10.0-3.0)/(n-1), 2)):
        positions1.append(round(j, 2))
    right = positions1  # towards Right
    print "right=", right
    left = sorted(right)  # towards left
    print "left=", left
    if a == 0 and s1 > min(up):  # up
        p.start(2.5)  # Initialising up down motor
        c = up.index(s1)
        d = up[c+1]
        print "d=", d
        p.ChangeDutyCycle(d)
        time.sleep(0.5)
    elif a == 0 and s1 <= min(up):
        print"UP motion not allowed"
    elif a == 1 and s1 < max(down):  # down
        p.start(2.5)
        c = down.index(s1)
        d = down[c+1]
        print "d=", d
        p.ChangeDutyCycle(d)
        time.sleep(0.5)
    elif a == 1 and s1 >= max(down):
        print"DOWN motion not allowed"
<<<<<<< HEAD
    elif a == 2 and s2 < max(left):  # left
        p1.start(2.5)
        c = left.index(s2)
        d = left[c+1]
        p1.ChangeDutyCycle(d)
        time.sleep(0.5)
    elif a == 2 and s2 >= max(left):
        print"Left motion not allowed"
    elif a == 3 and s2 > min(right):  # Right
=======
    elif a == 2 and s2 > min(right):  # Right
>>>>>>> 93de3c86483e3920b69fa021ad41c8736787a7a3
        p1.start(2.5)
        c = right.index(s2)
        d = right[c+1]
        p1.ChangeDutyCycle(d)
        time.sleep(0.5)
<<<<<<< HEAD
    elif a == 3 and s2 <= min(right):
        print"Right motion not allowed"

=======
    elif a == 2 and s2 <= min(right):
        print"Right motion not allowed"
    elif a == 3 and s2 < max(left):  # left
        p1.start(2.5)
        c = left.index(s2)
        d = left[c+1]
        p1.ChangeDutyCycle(d)
        time.sleep(0.5)
    elif a == 3 and s2 >= max(left):
        print"Left motion not allowed"
>>>>>>> 93de3c86483e3920b69fa021ad41c8736787a7a3


action(3, 5.0, 10.0)
