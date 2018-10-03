def frange(start, end, n):
    # step = round(step,3)
    tmp = start
    step = (end - start) / (n-1)
    for i in range(0, n):
        yield tmp
        tmp += step
