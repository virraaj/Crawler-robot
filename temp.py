import pinSetup
import time
import gotopos
import action_21 as act
pinVar = pinSetup.pinSetup()
p = pinVar[0]
p1 = pinVar[1]
encoder = pinVar[2]
ENClast = pinVar[3]
p.start(4.0)
p1.start(10.0)
#time.sleep(0.1)
#while True:
#    p1.ChangeDutyCycle(10.0)
'''
for x in range(0, 200):
    # y = mx+c
    c = 3.0
    m = 7.0 / 200.0
    y = m * x + c
    p1.ChangeDutyCycle(y)
    time.sleep(0.05)

gotopos.gotopos(2,0,p,p1, 3)
time.sleep(0.3)
ENClast = encoder.getData()
time.sleep(0.0)
act.playAction(3,2,0,3,p,p1)
time.sleep(0.5)
ENC = encoder.getData()
print (ENC - ENClast)
'''
while True:
    print (encoder.getData())
    gotopos.gotopos(2,0,p,p1,3)
    time.sleep(0.1)
    for x in range(0,200):
	c = 8.0
	m = -11 / 200.0
	y = m*x + c
	p1.ChangeDutyCycle(8.5)
	time.sleep(0.005)

'''
t = 0.1
while True:
    gotopos.gotopos(2, 2, p, p1, 3)
    time.sleep(0.3)
    ENClast = encoder.getData()
    time.sleep(0.0)
    act.playAction(2, 2, 2, 3, p, p1)
    time.sleep(t)
    ENC = encoder.getData()
    print ("act 1 =", ENC - ENClast)

    ENClast = encoder.getData()
    time.sleep(0.0)
    act.playAction(3, 2, 1, 3, p, p1)
    time.sleep(t)
    ENC = encoder.getData()
    print ("act 2 =", ENC - ENClast)

    ENClast = encoder.getData()
    time.sleep(0.0)
    act.playAction(1, 1, 2, 3, p, p1)
    time.sleep(t)
    ENC = encoder.getData()
    print ("act 3 =", ENC - ENClast)

    ENClast = encoder.getData()
    time.sleep(0.0)
    act.playAction(2, 2, 2, 3, p, p1)
    time.sleep(t)
    ENC = encoder.getData()
    print ("act 4 =", ENC - ENClast)

    ENClast = encoder.getData()
    time.sleep(0.0)
    act.playAction(2, 2, 1, 3, p, p1)
    time.sleep(t)
    ENC = encoder.getData()
    print ("act 5 =", ENC - ENClast)

    ENClast = encoder.getData()
    time.sleep(0.0)
    act.playAction(0, 2, 0, 3, p, p1)
    time.sleep(t)
    ENC = encoder.getData()
    print ("act 6 =", ENC - ENClast)
'''
# gotopos.gotopos(2,2,p,p1, 3)
# time.sleep(0.1)
# ENClast = encoder.getData()
# action_20.playAction(2,2,2,3,p,p1)
# time.sleep(0.1)
# ENC = encoder.getData()
# print (ENC - ENClast)
