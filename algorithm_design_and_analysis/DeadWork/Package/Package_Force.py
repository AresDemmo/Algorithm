import math
import os
import numpy
import queue
import random
import copy
import datetime


inFilename = 'algorithm_design_and_analysis/DeadWork/data/Package.txt'
outFilename = 'algorithm_design_and_analysis/DeadWork/Output/Package_Force.txt'

def Merge(S1, S2):
    answer = [[0, 0]]
    len1 = len(S1)
    len2 = len(S2)
    i = j = 0
    while i < len1 and j < len2:
        a1, a2 = S1[i], S2[j]
        a3 = answer[len(answer) - 1]
        if (a1[0] < a2[0] or (a1[0] == a2[0] and a1[1] >= a2[1])):
            if (a1[0] > a3[0] and a1[1] > a3[1]):
                answer += [a1]
            i += 1
        elif (a1[0] > a2[0] or (a1[0] == a2[0] and a1[1] <= a2[1])):
            if (a2[0] > a3[0] and a2[1] > a3[1]):
                answer += [a2]
            j += 1
    while i < len1:
        a1 = S1[i]
        a3 = answer[len(answer) - 1]
        if (a1[0] > a3[0] and a1[1] > a3[1]):
            answer += [a1]
        i += 1
    while j < len2:
        a2 = S2[j]
        a3 = answer[len(answer) - 1]
        if (a2[0] > a3[0] and a2[1] > a3[1]):
            answer += [a2]
        j += 1
    return answer

def Package_Force(A, C):
    cnt = [[0,0]]
    value = 0
    for i in range(len(A)):
        cns = []
        for j in range(len(cnt)):
            if (A[i][0] + cnt[j][0] <= C):
                cns += [[A[i][0] + cnt[j][0], A[i][1] + cnt[j][1]]]
                value = max(value, A[i][1] + cnt[j][1])
        cnt = Merge(cnt, cns)
        if (len(cnt) > 10000000):
            return -1
    return value



if __name__ == '__main__':
    outf = open(outFilename, "w")
    with open(inFilename) as data:
        T = int(data.readline())
        haha = 0
        for i in range(T):
            n = int(data.readline())
            C = int(data.readline())
            A = [[0, 0]]
            for i in range(n):
                w = int(data.readline())
                q = int(data.readline())
                A += [[w, q]]
                haha += w
            starttime = datetime.datetime.now()
            value = Package_Force(A, C)
            endtime = datetime.datetime.now()
            time = (endtime - starttime).seconds
            print(n, time, value, file=outf)
            print(n, time, value, C, haha)


