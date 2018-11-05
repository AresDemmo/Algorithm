
import numpy

def printINf(k):
    if k == 77777777:
        return 'inf'
    return k

def MachineSchedule(A, B, n):
    k = min(sum(A), sum(B))
    dp = numpy.zeros((n + 1, k + 1), dtype=int)
    inf = 77777777
    for i in range(len(dp)):
        for j in range(len(dp[0])):
            dp[i][j] = inf
    dp[0][0] = 0
    answer = k
    for i in range(n):
        for j in range(k + 1):
            if (j + A[i] <= k):
                dp[i + 1][j] = min(dp[i + 1][j], dp[i][j] + B[i])
                dp[i + 1][j + A[i]] = min(dp[i + 1][j + A[i]], dp[i][j])
    for i in range(k + 1):
        answer = min(answer, max(dp[n][i], i))
    for i in range(len(dp)):
        for j in range(len(dp[0])):
            print printINf(dp[i][j]),
        print
    print answer
    pass


if __name__ == '__main__':
    A = [2, 5, 7, 10, 5, 2]
    B = [3, 8, 4, 11, 3, 4]
    n = len(A)
    MachineSchedule(A, B, n)