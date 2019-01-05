import numpy
import random
import os
import Queue
from Queue import PriorityQueue
import datetime

LasStart = 5

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
table = 0

class Node(object):
    def __init__(self, x, y, deep):
        self.x = x
        self.y = y
        self.deep = deep
    def __lt__(self, others):
        return self.deep < others.deep

def LasVagas():
    cnt = numpy.zeros((n, m))
    for i in range(n):
        for j in range(m):
            if (table[i][j] == 'a'):
                startx, starty = i, j
            if (table[i][j] == 'b'):
                endx, endy = i, j
    que = PriorityQueue()
    que.put(Node(startx, starty, 0))
    cnt[startx][starty] = 1
    isLas = 0

    NodeNum = 0
    value = -1

    while not que.empty():
        node = que.get()
        NodeNum += 1
        if (node.x == endx and node.y == endy):
            value = node.deep
            break
        k = random.randint(0, 3)
        if isLas == 0 and que.qsize() > 40:
            isLas = LasStart
        for i in range(4):
            if isLas > 0 and i != k:
                continue            
            nx = node.x + dx[i]
            ny = node.y + dy[i]
            if (nx < 0 or nx >= n or ny < 0 or ny >= m):
                continue
            if (cnt[nx][ny] == 0 and table[nx][ny] != '1'):
                cnt[nx][ny] = node.deep + 1
                que.put(Node(nx, ny, node.deep + 1))
        if isLas > 0:
            isLas -= 1
    return (NodeNum, value)

if __name__ == '__main__':
    outf = open('eleTable', 'w')
    with open('data.txt') as data:
        T = int(data.readline())
        for i in range(T):
            n = int(data.readline())
            m = int(data.readline())
            print(n, m)
            table = []
            for j in range(n):
                table += [data.readline()]
            sumTime = sumNode = success = sumValue = 0
            for j in range(100):
                starttime = datetime.datetime.now()
                (nodes, value) = LasVagas()
                endtime = datetime.datetime.now()
                time=  (endtime - starttime).seconds
                print(i, j)
                sumTime += time
                sumNode += nodes
                if (value != -1):
                    sumValue += value
                    success += 1

            print >> outf, sumTime, sumNode, success, sumValue
            print sumTime, sumNode, success, sumValue
            

