import pinSetup
import time
import gotopos
import action_20
pinVar = pinSetup.pinSetup()
p = pinVar[0]
p1 = pinVar[1]
encoder = pinVar[2]
ENClast = pinVar[3]
i=1
'''
try:
    while True:
	ENC = encoder.getData()
        print ENC
        time.sleep(0.05)
except KeyboardInterrupt:
    print('interrupted!')
'''

p.start(4.0)
p1.start(6.5)
gotopos.gotopos(2,2,p,p1)
encoder.setData(0)
time.sleep(2.0)
action_20.playAction(1, 1, 1, 3, p, p1)
time.sleep(0.25)
ENC = encoder.getData()
print ENC
action_20.playAction(2, 2, 1, 3, p, p1)
time.sleep(0.25)
ENC = encoder.getData()
print ENC
time.sleep(2.05)
