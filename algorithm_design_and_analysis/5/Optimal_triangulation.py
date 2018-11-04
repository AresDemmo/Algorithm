
import numpy

def dis(x1, y1, x2, y2):
    return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5

def Triangulation(X, Y):
    n = len(X)
    inf = 0x3ffffffff
    d = numpy.zeros((n, n))
    dp = numpy.zeros((n, n))
    for i in range(n):
        for j in range(n):
            d[i][j] = dis(X[i], Y[i], X[j], Y[j])
            dp[i][j] = 0 if i == j else inf

    for i in range(1, n - 1):
        for j in range(1, n - i):
            l, r = j, j + i
            for k in range(l, r):
                dp[l][r] = min(dp[l][k] + dp[k + 1][r] + d[l - 1][k] + d[k][r] + d[l - 1][r], dp[l][r])
            print l, r, dp[l][r]
    print dp
    return dp


if __name__ == '__main__':
    X = [0, 1, 0, -1, 0]
    Y = [0, 1, 2, 1, 0]
    Triangulation(X, Y)