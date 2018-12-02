'''
____________________________________________________________________________
*** To bring both arms in required position independt of start postion. ***
--> required input arguments are
                raw = target raw index (position of second arm)
                col = target col index (position of first arm)
                p, p1 = handles to control servo motors (activated GPIOS)
                n = total nos of raw or col or states
______________________________________________________________________________
'''

# ___________ impoering dependencies ___________ #
import time


def gotopos(raw, col, p, p1, n):

    # ___________ sub method definition ___________ #
    def frange(start, end, n):
        tmp = start
        step = (end - start) / (n-1)
        for i in range(0, n):
            yield tmp
            tmp += step
    # ___________ sub method definition end ___________ #

    positions = []  # list initialization
    positions1 = []  # list initialization

    for i in frange(6.3, 3.0, n):  # range of first motor
        positions.append(i)
    positions.sort()

    for j in frange(8.5, 3.5, n):  # range of second motor
        positions1.append(j)

    time.sleep(0.05)
    p.ChangeDutyCycle(positions[raw])  # setting up first motor position
    time.sleep(0.1)
    p1.ChangeDutyCycle(positions1[col])  # setting up second motor position
    time.sleep(0.1)
