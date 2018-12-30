import numpy
import os
import math
import random
import itertools
import datetime
import copy


inFilename = 'algorithm_design_and_analysis/DeadWork/data/TSP.txt'
outFilename = 'algorithm_design_and_analysis/DeadWork/Output/TSP_Force.txt'
n = 0
table = 0

def CalCulate_length(p):
    cost = 0
    for i in range(1, n):
        cost += table[p[i - 1]][p[i]]
    cost += table[p[n - 1]][p[0]]
    return cost

def TSP_Force():
    path = [i for i in range(n)]
    cost = CalCulate_length(path)
    for i in itertools.permutations(path, n):
        c = CalCulate_length(i)
        if c < cost:
            cost = c
            path = copy.deepcopy(i)
    return (cost, path)


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
            if (n > 10 or n <= 1):
                continue
            starttime = datetime.datetime.now()
            (cost, path) = TSP_Force()
            endtime = datetime.datetime.now()
            time = (endtime - starttime).seconds
            print(n, time, cost, file=outf)