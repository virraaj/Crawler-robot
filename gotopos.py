#import RPi.GPIO as GPIO
import pinSetup
import time
def gotopos(s, s1, p, p1):
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

    print 'lr=',positions1
    print positions[s]
    print positions1[s1]
    #p.start(2.5)
    #p1.start(2.5)
    p.ChangeDutyCycle(positions[s])
    time.sleep(0.5)
    p1.ChangeDutyCycle(positions1[s1])
    time.sleep(0.5)
    #GPIO.cleanup()

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
