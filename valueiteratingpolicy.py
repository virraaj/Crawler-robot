import ValueIteration
import pinSetup
import action_22 as act
import gotopos
import initvalact
import time
import rewardsegregation_20 as rewardsegregation

'''
pinVar = pinSetup.pinSetup()
p = pinVar[0]
p1 = pinVar[1]
encoder = pinVar[2]
ENClast = pinVar[3]

p.start(10.0)
p1.start(10.0)
'''


def valueiteratingpolicy(n):
    v = initvalact.initvalact(n)
    value = v[0]
    action = v[1]
    reward = rewardsegregation.rewardsegregation(n, p, p1, encoder, ENClast)
    print reward
    test = ValueIteration.valueiteration(value, reward, action)
    policy = test[1]
    print policy
    raw = 0
    col = 0
    gotopos.gotopos(raw, col, p, p1, n)
    # 0 = up / 1 = down / 2 = left / 3= right
    global val1
    val1 = pinSetup.valueRead_ON()
    while True and val1 == 0:
        if action[raw][col] == 0:
            act.playAction(0, raw, col, n, p, p1)
            raw = raw - 1

        elif action[raw][col] == 1:
            act.playAction(1, raw, col, n, p, p1)
            raw = raw + 1

        elif action[raw][col] == 2:
            act.playAction(2, raw, col, n, p, p1)
            col = col - 1

        elif action[raw][col] == 3:
            act.playAction(3, raw, col, n, p, p1)
            col = col + 1
        val1 = pinSetup.valueRead_ON()
    if val1 == 1:
        print "Stop"

        #import os
        #os.system("shutdown now")
valueiteratingpolicy(3)
