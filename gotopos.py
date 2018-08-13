def gotopos(s,s1):
    servoPIN = 17
    servoPIN1 = 4
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(servoPIN, GPIO.OUT)
    GPIO.setup(servoPIN1, GPIO.OUT)
    p = GPIO.PWM(servoPIN, 50) # GPIO 17 als PWM mit 50Hz
    p1 = GPIO.PWM(servoPIN1, 50)
    p.start(2.5)
    p1.start(2.5)

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
    #print positions[0]
    #print positions1[0]
    p.ChangeDutyCycle(m)
    p1.ChangeDutyCycle(n)
#gotopos(0,0)
