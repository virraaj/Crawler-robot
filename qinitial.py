from copy import deepcopy
def qinitial(n):

    #value = [[[0]*4]*n for i in range(n)]
    #action = [[None]*n for i in range(n)]
    a = [0,0,0,0]
    temp = []
    value = []
    for i in range(1,n+1):
        temp.append(deepcopy(a))
    for j in range(1,n+1):
	value.append(deepcopy(temp))
    return value
q = qinitial(3)
print q
q[0][0][0] = 11
print q
