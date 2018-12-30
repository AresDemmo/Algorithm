import math
import os
import numpy
import queue
import random
import copy
import datetime

inFilename = 'algorithm_design_and_analysis/DeadWork/data/TSP.txt'
outFilename = 'algorithm_design_and_analysis/DeadWork/Output/TSP_SA.txt'
n = 0
table = numpy.empty((0, 0), dtype=int)
Speed = 0.9
Initial_Temp = 1000.0
L = 10


class Node(object):
    def __init__(self, length, path):
        self.length = length
        self.path = copy.deepcopy(path)

    def copy(self, length, path):
        self.length = length
        self.path = copy.deepcopy(path)

def CalCulate_length(p):
    cost = 0
    for i in range(1, n):
        cost += table[p[i - 1]][p[i]]
    cost += table[p[n - 1]][p[0]]
    return cost


def getNewSolution(temp):
    i = j = 0
    while i == j:
        i, j = random.randint(0, n - 1), random.randint(0, n - 1)
    #swap
    t = temp.path[i]
    temp.path[i] = temp.path[j]
    temp.path[j] = t


def Accept(bestone, temp, t):
    if (bestone.length > temp.length):
         return True
    else :
        if int(math.exp((bestone.length - temp.length) / t) * 100) > random.randint(0, 100):
            return True
    return False



def TSP_SA():
    r, t, t_min = Speed, Initial_Temp, 0.001
    p = [i for i in range(n)]
    cost = CalCulate_length(p)
    temp, bestone = Node(cost, p), Node(cost, p)
    while t > t_min:
        for i in range(L):
            getNewSolution(temp)
            temp.length = CalCulate_length(temp.path)
            if (Accept(bestone, temp, t)):
                bestone.copy(temp.length, temp.path)
            else:
                temp.copy(bestone.length, bestone.path)
        t *= r
    return (bestone.length, bestone.path)

if __name__ == '__main__':

    outf = open(outFilename, "w")
    with open(inFilename) as data:
        T = int(data.readline())
        for i in range(T):
            n = int(data.readline())
            table = numpy.empty((n, n), dtype=int)
            for A in range(n):
                for B in range(n):
                    table[A][B] = int(data.readline())
            L = 100 * n
            if (n <= 1):
                continue
            starttime = datetime.datetime.now()
            (cost, path) = TSP_SA()
            endtime = datetime.datetime.now()
            time = (endtime - starttime).seconds
            print(n, time, cost, file=outf)


"""
 n = 3
table = [[0, 1, 2],[1,0,4],[2,3,0]]
test()
very small data
3
0 1 2
1 0 4
2 3 0
"""