import pinSetup
import time
import gotopos
import action_20
pinVar = pinSetup.pinSetup()
p = pinVar[0]
p1 = pinVar[1]
encoder = pinVar[2]
ENClast = pinVar[3]
val1 = pinSetup.valueRead()
p.start(4.25)
p1.start(10.0)
time.sleep(0.1)
'''
#for x in range(0, 200):
    # y = mx+c
    c = 3.0
    m = 7.0 / 200.0
    y = m * x + c
    p1.ChangeDutyCycle(y)
    time.sleep(0.05)
'''
while True:
    print "v=", val1
    if val1 == 0:
	print "0"
    else:
	print "1"
    time.sleep(1)
    val1 = pinSetup.valueRead()
