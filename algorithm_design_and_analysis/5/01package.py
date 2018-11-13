import numpy

def compare(b1, v1, b2, v2):
    if (b1 >= b2 and v1 < v2):
        return False
    return True

def Merge(S1, S2):
    answer = []
    len1 = len(S1)
    len2 = len(S2)
    i = j = 0
    while i < len1 and j < len2:
        a1, a2 = S1[i], S2[j]
        if (compare(a1[0], a1[1], a2[0], a2[1])):
            answer += [a1]
            i += 1
        else :
            answer += [a2]
            j += 1
    while i < len1:
        a1 = S1[i]
        a2 = answer[len(answer) - 1]
        if (compare(a1[0], a1[1], a2[0], a2[1])):
            answer += [a1]
        i += 1
    while j < len2:
        a1 = S2[j]
        a2 = answer[len(answer) - 1]
        if (compare(a1[0], a1[1], a2[0], a2[1])):
            answer += [a1]
        j += 1
    return answer


def DKpackageExtend(W, P, C, n, m):
    B = numpy.zeros(m)
    V = numpy.zeros(m)
    resB = numpy.zeros(m)
    resV = numpy.zeros(m)
    B[1] = V[1] = 0
    s = t = 1
    cnt = 2
    for i in range(n):
        w, p = W[i], P[i]
        for j in range(s, t + 1):
            resB[j], resV[j] = B[j] + w, V[j] + p
        k1, k2 = s + 1, s
        B[cnt], V[cnt] = 0, 0
        while (k1 <= t or k2 <= t):
            if (k2 > t) or (k1 <= t and k2 <= t and compare(B[k1], V[k1], resB[k2], resV[k2])):
                if (compare(B[k1], V[k1], B[cnt], V[cnt])):
                    cnt += 1
                    B[cnt], V[cnt] = B[k1], V[k1]
                k1 += 1
            else :
                if (compare(resB[k2], resV[k2], B[cnt], V[cnt])):
                    cnt += 1
                    B[cnt], V[cnt] = resB[k2], resV[k2]
                k2 += 1
            if (B[cnt] > C):
                cnt -= 1
                break
        cnt += 1
        s , t = t + 1, cnt - 1
    return V[cnt - 1]


def DKpackageClassical(W, P, C, n, m):
    B = numpy.zeros(m)
    V = numpy.zeros(m)
    resB = numpy.zeros(m)
    resV = numpy.zeros(m)
    B[1] = V[1] = 0
    s = t = 1
    cnt = 2
    for i in range(n):
        w, p = W[i], P[i]
        for j in range(s, t + 1):
            resB[j], resV[j] = B[j] + w, V[j] + p
        k1, k2 = s + 1, s
        B[cnt], V[cnt] = 0, 0
        while (k1 <= t or k2 <= t):
            if (k2 > t) or (k1 <= t and k2 <= t and compare(B[k1], V[k1], resB[k2], resV[k2])):
                if (compare(B[k1], V[k1], B[cnt], V[cnt])):
                    cnt += 1
                    B[cnt], V[cnt] = B[k1], V[k1]
                k1 += 1
            else :
                if (compare(resB[k2], resV[k2], B[cnt], V[cnt])):
                    cnt += 1
                    B[cnt], V[cnt] = resB[k2], resV[k2]
                k2 += 1
            if (B[cnt] > C):
                cnt -= 1
                break
        cnt += 1
        s , t = t + 1, cnt - 1
    return V[cnt - 1]
    

def Merge2(A, B, C):
    return Merge(A, Merge(B, C))

def DKpackageEx(A, C):
    cnt = [[0,0]]
    answer = []
    answer += [cnt]
    for i in range(len(A)):
        cns = []
        cns1 = []
        for j in range(len(cnt)):
            if (A[i][0] + cnt[j][0] <= C):
                cns += [[A[i][0] + cnt[j][0], A[i][1] + cnt[j][1]]]
            if (A[i][0] + 2 * cnt[j][0] <= C):
                cns1 += [[A[i][0] + 2 * cnt[j][0], A[i][1] + 2 * cnt[j][1]]]
        cnt = Merge2(cnt, cns, cns1)
        answer += [cnt]
    print answer
    return answer

def DKpackage(A, C):
    answer = []
    cnt = [[0,0]]
    answer += [cnt]
    haha = 0
    for i in range(len(A)):
        cns = []
        for j in range(len(cnt)):
            if (A[i][0] + cnt[j][0] > C):
                break
            cns += [[A[i][0] + cnt[j][0], A[i][1] + cnt[j][1]]]
            haha = max(haha, A[i][1] + cnt[j][1])
        cnt = Merge(cnt, cns)
        answer += [cnt]
    print haha
    return answer



if __name__ == '__main__':
    """
    W = [0, 4, 6, 8, 3, 1, 1, 4, 5, 5, 7, 7, 8, 3, 7, 9, 9, 10, 8, 10, 6]
    P = [0, 1, 5, 1, 8, 4, 8, 7, 4, 6, 1, 4, 4, 5, 5, 7, 1, 8, 2, 7, 1]
    A = []
    for i in range(1, len(W)):
        A += [[W[i], P[i]]]
    print A
    C = 50
    DKpackage(A, C)
    """


    W = [0, 4, 6, 8, 3, 1, 1, 4, 5, 5, 7, 7, 8, 3, 7, 9, 9, 10, 8, 10, 6]
    P = [0, 1, 5, 1, 8, 4, 8, 7, 4, 6, 1, 4, 4, 5, 5, 7, 1, 8, 2, 7, 1]
    c = 50
    n = 20
    m = 2 ** (4 + 1)
    m1 = 3 ** (4 + 1)
    print DKpackageClassical(W, P, c, n, m)
    #print DKpackageClassical(w, p, c, n, m1)

"""
0,0 1,2 2,3 3,5
3,2 4,4 5,5 6,7

"""