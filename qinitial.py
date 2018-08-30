def qinitial(n):

    #value = [[[0]*4]*n for i in range(n)]
    #action = [[None]*n for i in range(n)]
    a = [0,0,0,0]
    for i in range(1,n+1):
        for j in range(1,n+1):

            value = [[a]*j]*i
    return value
print qinitial(3)
