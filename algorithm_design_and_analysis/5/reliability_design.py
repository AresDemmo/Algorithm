
import numpy

def reliability_design(g, c, Cost):
    g = [0] + g
    c = [0] + c
    n = len(g)
    dp = numpy.zeros((n, Cost + 1))
    for i in range(len(dp[0])): dp[0][i] = 1.0
    for i in range(1, n):
        for j in range(1, Cost + 1):
            for k in range(1, j // c[i] + 1):
                dp[i][j] = max(dp[i][j], min(dp[i - 1][j - k * c[i]], 1.0 - (1.0 - g[i]) ** k))
    print dp
    return dp[n - 1][Cost]

if __name__ == '__main__':
    g = [0.8, 0.7, 0.6]
    c = [8, 7, 6]
    Cost = 30
    print reliability_design(g, c, Cost)