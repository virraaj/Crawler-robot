#import ipdb
import GoToHome
import generate_rewardmatrix
import pinSetup
import gotopos
import action_22 as act
import time
t = 0.1
# 0 = up / 1 = down / 2 = left / 3= right


def action_select(raw, col, n):
    # action selection according to selction of state
    if raw == 0 and col == 0:
        return [1, 3]
    elif raw == 0 and (col == -1 or col == n-1):
        return [1, 2]
    elif raw == 0:
        return [1, 2, 3]

    elif raw == n-1 and col == 0:
        return [0, 3]
    elif raw == n-1 and (col == -1 or col == n-1):
        return [0, 2]
    elif raw == n-1:
        return [0, 2, 3]

    elif col == 0:
        return [0, 1, 3]
    elif (col == -1 or col == n-1):
        return [0, 1, 2]

    else:
        return [0, 1, 2, 3]  # cells where all four actions are possible


def rewardsegregation(n, p, p1, encoder, ENClast):
    reward = generate_rewardmatrix.generate_rewardmatrix(n)
    for raw in range(0, n):
        for col in range(0, n):
            for action in action_select(raw, col, n):
                gotopos.gotopos(raw, col, p, p1, n)
                time.sleep(0.3)
                ENClast = encoder.getData()
                act.playAction(action, raw, col, n, p, p1)
                time.sleep(t)
                if action == 0 or action == 1:
                    ENClast = encoder.getData()
                ENC = encoder.getData()
		direction = pinSetup.valueRead_dir()
		print ((-1)**direction)*(ENC - ENClast)
                reward[raw][col][action] = ((-1)**direction)*(ENC - ENClast)
                time.sleep(0.05)
	    time.sleep(0.1)
	time.sleep(0.1)
    return reward

'''
pinVar = pinSetup.pinSetup()
p = pinVar[0]
p1 = pinVar[1]
encoder = pinVar[2]
ENClast = pinVar[3]
p.start(4.0)
p1.start(6.5)
encoder.setData(0)
#GoToHome.GoToHome(p, p1)
#time.sleep(0.25)
#gotopos.gotopos(0,0,p,p1)
#gotopos.gotopos(1,0,p,p1)
#gotopos.gotopos(2,0,p,p1)
#time.sleep(0.25)
#action_20.playAction(0,1,0,3,p,p1)
#time.sleep(0.25)
reward = rewardsegregation(4, p, p1, encoder, ENClast)
print reward
#print reward[1]
#print reward[2]

'''
