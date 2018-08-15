
def frange(start, end, step):
    tmp = start
    while(tmp >= end):
        yield tmp
        tmp -= step
n = 4
#while True:
#for i in frange(10,2.5,(10.0-2.5)/(n-1)):
 #   print i

for j in frange(10.0,2.5,(10.0-2.5)/(n-1)):
           
    print j



