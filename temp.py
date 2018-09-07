import pinSetup
import time
import gotopos
import action_21 as act
pinVar = pinSetup.pinSetup()
p = pinVar[0]
p1 = pinVar[1]
encoder = pinVar[2]
ENClast = pinVar[3]
p.start(10.0)
p1.start(10.0)
#time.sleep(0.1)
'''
for x in range(0, 200):
    # y = mx+c
    c = 3.0
    m = 7.0 / 200.0
    y = m * x + c
    p1.ChangeDutyCycle(y)
    time.sleep(0.05)
'''
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
    action_21.playAction(3,3,1,5,p,p1)
    time.sleep(0.1)
    action_21.playAction(2,3,2,5,p,p1)
    time.sleep(0.1)
'''
# gotopos.gotopos(2,2,p,p1, 3)
# time.sleep(0.1)
# ENClast = encoder.getData()
# action_20.playAction(2,2,2,3,p,p1)
# time.sleep(0.1)
# ENC = encoder.getData()
# print (ENC - ENClast)
