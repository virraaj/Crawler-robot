import numpy as np


def error(v1, v2):
    s1 = np.shape(v1)
    s2 = np.shape(v2)
    if s1 == s2:
        err = 0
        for r in range(0, s1[0]):
            for c in range(0, s1[1]):
                err = err + (v1[r][c] - v2[r][c]) ** 2
        return err


def qError(v1, v2):
    s1 = np.shape(v1)
    s2 = np.shape(v2)
    if s1 == s2:
        err = 0
        for r in range(0, s1[0]):
            for c in range(0, s1[1]):
                for a in range(0, s1[2]):
                    err = err + (v1[r][c][a] - v2[r][c][a]) ** 2
        return err


# v1 = [[1, 0, 1], [0, 0, 0], [1, 1, 1]]
# v2 = [[0.99, 0, 0.99], [0, 0.001, 0], [0.99, 0.999, 1]]
# e = error(v1, v2)
# print (e)
# Q = [[[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]],  # State1,State2, Stete3
#      [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]],  # State4, State5, State6
#      [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]]
# Qnew = [[[1, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]],  # State1,State2, Stete3
#         [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 1, 0]],  # State4, State5, State6
#         [[0, 0, 0, 0], [1, 0, 0, 0], [0, 0, 0, 0]]]
# print(qError(Q, Qnew))
