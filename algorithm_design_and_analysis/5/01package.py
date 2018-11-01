import numpy

def main(A, D):
    n = len(A)
    dp = numpy.zeros((n + 1, D + 1), dtype=int)
    answer = 0
    for i in range(1, n + 1):
        for j in range(1, D + 1):
            if j < A[i - 1][0]:
                dp[i][j] = dp[i - 1][j]
            else: 
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - A[i - 1][0]] + A[i - 1][1])
            answer = max(answer, dp[i][j])
    return answer
    

if __name__ == '__main__':
    A = [[1, 2], [2, 3], [3, 2], [3, 5]]
    D = 3
    print main(A, D)