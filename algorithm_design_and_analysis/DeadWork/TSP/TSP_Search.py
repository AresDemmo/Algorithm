import numpy
import os
import datetime
from queue import PriorityQueue
import copy

inFilename = 'algorithm_design_and_analysis/DeadWork/data/TSP.txt'
outFilename = 'algorithm_design_and_analysis/DeadWork/Output/TSP_Search.txt'
n = 0
table = 0

class Node(object):
    def __init__(self, cost, deep, path):
        self.cost = cost
        self.deep = deep
        self.path = copy.deepcopy(path)
    def __lt__(self, other):#operator < 
        return self.cost < other.cost
    def __cmp__(self,other):
        #call global(builtin) function cmp for int
        return self.cost < self.cost
    def __str__(self):
        return (self.cost, self.deep, self.path)
    def copy(self, a):
        self.cost = a.cost
        self.deep = a.deep
        self.path = copy.deepcopy(a.path)

def TSP_Search():
    ans = Node(n * 1000, n, [])
    a = Node(0, 1, [0])
    que = PriorityQueue()
    que.put(Node(0, 1, [0]))
    while not que.empty():
        node = que.get()
        A = node.path[node.deep - 1]
        if node.deep == n:
            if node.cost + table[A][0] < ans.cost:
                ans.copy(node)
                ans.cost = node.cost + table[A][0]
            continue
        for i in range(n):
            if not i in node.path:
                cost = node.cost + table[A][i]
                if cost < ans.cost:
                    que.put(Node(cost, node.deep + 1, node.path + [i]))
    return (ans.cost, ans.path)




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
            if (n > 15 or n <= 1):
                continue
            starttime = datetime.datetime.now()
            (cost, path) = TSP_Search()
            endtime = datetime.datetime.now()
            time = (endtime - starttime).seconds
            print(n, time, cost, file=outf)