import pinSetup
import time
import gotopos
import action_21 as act
pinVar = pinSetup.pinSetup()
p = pinVar[0]
p1 = pinVar[1]
encoder = pinVar[2]
ENClast = pinVar[3]
#p.start(4.0)
#p1.start(10.0)
#time.sleep(0.1)
while True:
    '''
    p1.ChangeDutyCycle(2.0)
    gotopos.gotopos(2,1,p,p1,3)
    time.sleep(1.0)
    e = encoder.getData()
    act.playAction(3,2,1,3,p,p1)
    time.sleep(1.0)
    el = encoder.getData()
    print el
    '''
    print pinSetup.valueRead_alg()
#    print pinSetup.valueRead_ON()
#    print pinSetup.valueRead_dir()
    print "\n"
    time.sleep(1.0)
