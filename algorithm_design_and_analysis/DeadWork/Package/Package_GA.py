import math
import os
import numpy
import queue
import random
import copy
import datetime

TSPFilename = 'algorithm_design_and_analysis/DeadWork/data/Package'
n, m = 0, 0
popsize = 200 #种群规模
pc = 0.618 #交配概率
pm = 0.03 #变异概率
lchrom = 50 #染色体长度
maxgen = 1000 #最大进化代数

class Node(object):
    def __init__(self, chrom, weight, fitness, parent1, parent2, cross):
        self.chrom = [0 for i in range(lchrom)]
        self.weight = weight

        

def readDate(filename):
    with open(TSPFilename + '/' + filename) as data:
        lines = data.readlines()

    global n, table, L
    n = int(lines[0])
    table = numpy.empty((n, n), dtype=int)
    for i in range(n):
        for j in range(n):
            table[i][j] = int(lines[i * n + j + 1])
    L = 100 * n
    return (n, table)



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
    return bestone






if __name__ == '__main__':
    files = os.listdir(TSPFilename)
    f = open("algorithm_design_and_analysis/DeadWork/Output/TSP_SA.txt", "w")
    for i in files:
        readDate(i)
        starttime = datetime.datetime.now()
        ans = TSP_SA()
        endtime = datetime.datetime.now()
        print("dataNum:", n, " time：", (endtime - starttime).seconds,"s", file=f)
        print(ans.length, file=f)
        print(ans.path, file=f)
        break


"""a

very small data
3 10
5 3
6 5
5 3
"""