# calculator the Divergence distance of two matrixs

import math

def Distance(A, B):
    """
        first examine two matrix is equal
        the sum of Alog(A/B)-A+B
        return the distance
        in order to avoid 0, every number add a small float
    """
    if len(A) != len(B):
        return 'two matrix have not equal length'
    sum = 0
    eps = 0.0000000001
    for i in range(len(A)):
        va, vb = A[i], B[i]
        if len(va) != len(vb):
            return 'two matrixs have not equal length'
        for j in range(len(va)):
            a, b = va[j] + eps, vb[j] + eps
            sum += a * math.log(a / b) - a + b;
    return sum

if __name__ == '__main__':
    Distance(A, B)
