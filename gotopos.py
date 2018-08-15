<<<<<<< HEAD
#import RPi.GPIO as GPIO
import pinSetup
import time
def gotopos(s, s1, p, p1):
    '''
=======
<<<<<<< HEAD
<<<<<<< HEAD
=======
import RPi.GPIO as GPIO
import time
>>>>>>> aa00730129355e5f8b05cc3100f8c95634d30c38
=======
import RPi.GPIO as GPIO
import time
>>>>>>> 0249eafa5b9d08f63eb7a4e5ba171841cff71049
def gotopos(s,s1):
>>>>>>> 9a9bf1e605a8626da96edcb1f9c1db353dc427bd
    servoPIN = 17
    servoPIN1 = 4
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(servoPIN, GPIO.OUT)
    GPIO.setup(servoPIN1, GPIO.OUT)
    p = GPIO.PWM(servoPIN, 50) # GPIO 17 als PWM mit 50Hz
    p1 = GPIO.PWM(servoPIN1, 50)
<<<<<<< HEAD
<<<<<<< HEAD
    p.start(2.5)
    p1.start(2.5)
=======
    #p.start(2.5)
    #p1.start(2.5)
>>>>>>> aa00730129355e5f8b05cc3100f8c95634d30c38
=======
    #p.start(2.5)
    #p1.start(2.5)
<<<<<<< HEAD
    '''
=======
>>>>>>> 0249eafa5b9d08f63eb7a4e5ba171841cff71049

>>>>>>> 9a9bf1e605a8626da96edcb1f9c1db353dc427bd
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

    print 'ud=',positions
    for j in frange(10.0,3.0,n):
        positions1.append(j)
    positions1.sort()

<<<<<<< HEAD
    print 'lr=',positions1
    print positions[s]
    print positions1[s1]
    #p.start(2.5)
    #p1.start(2.5)
=======
    #print 'lr=',positions1
<<<<<<< HEAD
<<<<<<< HEAD
    #print positions[0]
    #print positions1[0]
    p.ChangeDutyCycle(m)
    p1.ChangeDutyCycle(n)
=======
=======
>>>>>>> 0249eafa5b9d08f63eb7a4e5ba171841cff71049
    print positions[s]
    print positions1[s1]
    p.start(2.5)
    p1.start(2.5)
<<<<<<< HEAD
    p.ChangeDutyCycle(positions[s])  # goes to position given in function
=======
>>>>>>> 9a9bf1e605a8626da96edcb1f9c1db353dc427bd
    p.ChangeDutyCycle(positions[s])
>>>>>>> 0249eafa5b9d08f63eb7a4e5ba171841cff71049
    time.sleep(0.5)
    p1.ChangeDutyCycle(positions1[s1])
    time.sleep(0.5)
    #GPIO.cleanup()

<<<<<<< HEAD
'''
pinVar = pinSetup.pinSetup()
p = pinVar[0]
p1 = pinVar[1]
encoder = pinVar[2]
ENClast = pinVar[3]
p.start(3.0)
p1.start(3.0)
gotopos(2,2,p,p1)
'''
=======
<<<<<<< HEAD
>>>>>>> aa00730129355e5f8b05cc3100f8c95634d30c38
=======
>>>>>>> 0249eafa5b9d08f63eb7a4e5ba171841cff71049
#gotopos(0,0)
>>>>>>> 9a9bf1e605a8626da96edcb1f9c1db353dc427bd
