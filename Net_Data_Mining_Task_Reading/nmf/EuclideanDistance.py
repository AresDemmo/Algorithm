# calculator the Euclidean distance of two matrixs

import math

def EucliDistance(A, B):
    """
        first examine two matrix is equal
        the ||A-B|| ^ 2 = sum((A_{ij} - B_{ij})^2)
        return dis^2
    """
    if len(A) != len(B):
        return 'two matrix have not equal length'
    sum = 0
    for i in range(len(A)):
        va, vb = A[i], B[i]
        if len(va) != len(vb):
            return 'two matrixs have not equal length'
        for j in range(len(va)):
            a, b = va[j], vb[j]
            sum += (a - b) ** 2;
    return sum

if __name__ == '__main__':
    A = [
        [1, 0, 0],
        [0, 1, 0],
        [0, 0, 1]
        ]
    B = [
        [1, 0, 0],
        [0, 1, 0],
        [0, 0, 1]
        ]
    print EucliDistance(A, B)
