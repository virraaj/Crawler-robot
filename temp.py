import action_20
# def frange(start, end, n):
#     # step = round(step,3)
#     tmp = start
#     step = (end - start) / (n-1)
#     for i in range(0, n):
#         yield tmp
#         tmp += step


n = 4
positions = []
for i in action_20.frange(3.0, 5.0, n):
    positions.append(round(i, 2))

up = positions
print up

# positions1 = []  # positions motor2
# for j in frange(3.0, 10.0, n):
#     positions1.append(round(j, 2))
# left = positions1
# print left
