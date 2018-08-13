<<<<<<< HEAD
=======
import RPi.GPIO as GPIO
import time
>>>>>>> aa00730129355e5f8b05cc3100f8c95634d30c38
def gotopos(s,s1):
    servoPIN = 17
    servoPIN1 = 4
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(servoPIN, GPIO.OUT)
    GPIO.setup(servoPIN1, GPIO.OUT)
    p = GPIO.PWM(servoPIN, 50) # GPIO 17 als PWM mit 50Hz
    p1 = GPIO.PWM(servoPIN1, 50)
<<<<<<< HEAD
    p.start(2.5)
    p1.start(2.5)
=======
    #p.start(2.5)
    #p1.start(2.5)
>>>>>>> aa00730129355e5f8b05cc3100f8c95634d30c38

    def frange(start, end, n):
        # step = round(step,3)
        tmp = start
        step = (end - start) / (n-1)
        for i in range(0, n):
            yield tmp
            tmp += step
    positions = []

    positions1 = []

    n = 5
    for i in frange(5.0,3.0,n):
        positions.append(i)
    positions.sort()

    #print 'ud=',positions
    for j in frange(10.0,3.0,n):
        positions1.append(j)
    positions1.sort()

    #print 'lr=',positions1
<<<<<<< HEAD
    #print positions[0]
    #print positions1[0]
    p.ChangeDutyCycle(m)
    p1.ChangeDutyCycle(n)
=======
    print positions[s]
    print positions1[s1]
    p.start(2.5)
    p1.start(2.5)
    p.ChangeDutyCycle(positions[s])  # goes to position given in function
    time.sleep(0.5)
    p1.ChangeDutyCycle(positions1[s1])
    time.sleep(0.5)
    GPIO.cleanup()

>>>>>>> aa00730129355e5f8b05cc3100f8c95634d30c38
#gotopos(0,0)
