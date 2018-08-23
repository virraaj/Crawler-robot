import pinSetup_temp
import time
import gotopos
import action_20
pinVar = pinSetup_temp.pinSetup()
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
gotopos.gotopos(2,2,p,p1, 3)
time.sleep(0.1)
ENClast = encoder.getData()
time.sleep(2.0)
action_20.playAction(2,2,2,3,p,p1)
time.sleep(0.1)
ENC = encoder.getData()
print (ENC - ENClast)
