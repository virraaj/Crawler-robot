# generateDummy method generates dummy list of same size with first element 1
import numpy as np


def generateDummy(v1):
    s = np.shape(v1)
    layer = len(s)
    List = []
    appendElement = 1
    cnt = 0
    for lyr in range(0, layer):
        cnt += 1
        List = []
        for ele in range(0, s[(layer-1) - lyr]):
            List.append(appendElement)
            if cnt == 1:
                appendElement = 0
        appendElement = List

    return List


# Trail vectors and print statements
# v1 = [[[10, 110, 10, 1110], [10, 110, 10, 1110], [10, 110, 10, 1110]],
#       [[10, 110, 10, 1110], [10, 110, 10, 1110], [10, 110, 10, 1110]],
#       [[10, 110, 10, 1110], [10, 110, 10, 1110], [10, 110, 10, 1110]]]
# v2 = [[0, 0, 0, 0], [0, 0, 0, 0]]
# print(generateDummy(v1))
# print ("\n")
# print(np.shape(v1), np.shape(generateDummy(v1)))
