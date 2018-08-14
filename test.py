#from KY040.ky040.KY040 import KY040

def frange(start, end, n):
    # step = round(step,3)
    tmp = start
    step = (end - start) / (n-1)
    for i in range(0, n):
        yield tmp
        tmp += step
n = 4
#while True:
#for i in frange(10,2.5,(10.0-2.5)/(n-1)):
 #   print i
'''for i in frange(5.0,2.5,(5.0-2.5)/(n-1)):
        for j in frange(10.0,2.5,(10.0-2.5)/(n-1)):
            print i
            print j'''
positions1 = []
a = frange(11.0,4.0,n)
print a

for j in frange(10.0,3.0,n):
    positions1.append(j)
    print j
print positions1
