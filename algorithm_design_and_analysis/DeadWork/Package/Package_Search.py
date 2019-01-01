from queue import PriorityQueue
import random
import math
import datetime
import numpy


inFilename = 'algorithm_design_and_analysis/DeadWork/data/Package.txt'
outFilename = 'algorithm_design_and_analysis/DeadWork/Output/Package_Search.txt'

class Node(object):
    def __init__(self, id, par, level, tag, CC, CV, CUB):
        self.id = id
        self.par = par
        self.level = level
        self.tag = tag
        self.CC = CC
        self.CV = CV
        self.CUB = CUB

    def __lt__(self, other):#operator < 
        return self.CUB > other.CUB


    def __str__(self):
        return ( self.id, self.par, self.level, self.tag, self.CC, self.CV, self.CUB)

tables = []

def getNode(par, level, tag, cc, cv, ub):
    global tables
    id = len(tables)
    node = Node(id, par, level, tag, cc, cv, ub)
    tables += [node]
    return node

def LUBound(P, W, cap, cv, N, k):
    rw = cap
    pvl = cv
    for i in range(k, N + 1):
        if rw < W[i]:
            pvu = pvl + 1.0 * rw * P[i] / W[i]
            for j in range(i + 1, N + 1):
                if rw >= W[j]:
                    rw = rw - W[j]
                    pvl = pvl + P[j]
            return (pvl, pvu)
        rw = rw - W[i]
        pvl = pvl + P[i]
    pvu = pvl
    return (pvl, pvu)


def DKpackage(P, W, N, M, e):
    global tables
    tables = []
    (pvl, pvu) = LUBound(P, W, M, 0, N, 1)
    node = getNode(0, 0, 0, M, 0, pvu)
    prev = pvl - e
    que = PriorityQueue()
    que.put(node)
    while not que.empty():
        node = que.get()
        i = node.level + 1
        cap = node.CC
        cv = node.CV
        if node.CUB <= prev:
            break
        if i == N + 1:
            if cv > prev:
                prev = cv
                answer = node
        else:
            if cap >= W[i]:
                cntnode = getNode(node.id, i, 1, cap - W[i], cv + P[i], node.CUB)
                que.put(cntnode)
            (pvl, pvu) = LUBound(P, W, cap, cv, N, i + 1)   
            if pvu > prev:
                cntnode = getNode(node.id, i, 0, cap, cv, pvl)  
                que.put(cntnode)
    return answer


class Pair(object):
    def __init__(self, w, p):
        self.w = w
        self.p = p
    def __lt__(self, Other):
        return 1.0 * self.p / self.w > 1.0 * Other.p / Other.w

if __name__ == '__main__':


    outf = open(outFilename, "w")
    with open(inFilename) as data:
        T = int(data.readline())
        for i in range(T):
            n = int(data.readline())
            C = int(data.readline())
            que = PriorityQueue()
            for i in range(n):
                w = int(data.readline())
                p = int(data.readline())
                que.put(Pair(w, p))
            W, P = [0], [0]
            while not que.empty():
                node = que.get()
                W += [node.w]
                P += [node.p]
            starttime = datetime.datetime.now()
            value = DKpackage(P, W, n, C, 0.01)
            endtime = datetime.datetime.now()
            time = (endtime - starttime).seconds
            print(n, time, value.CV,file=outf)
            print(n, time, value.CV)
