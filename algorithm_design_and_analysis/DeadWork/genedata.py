import random
import numpy
import os
from Queue import PriorityQueue




dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

class Node(object):
    def __init__(self, x, y, deep):
        self.x = x
        self.y = y
        self.deep = deep
    def __lt__(self, other):
        return self.deep < other.deep


def EleTable(A, n, m):
    for i in range(n):
        for j in range(m):
            if (A[i][j] == 'a'):
                startx, starty = i, j
            elif (A[i][j] == 'b'):
                endx, endy = i, j
    table = numpy.zeros((n, m))
    que = PriorityQueue()
    table[startx][starty] = 1
    que.put(Node(startx, starty, 1))
    while not que.empty():
        node = que.get()
        if (node.x == endx and node.y == endy):
            return node.deep - 1
        for i in range(4):
            nx = node.x + dx[i]
            ny = node.y + dy[i]
            if (nx < 0 or nx >= n or ny < 0 or ny >= m):
                continue
            if (table[nx][ny] == 0 and A[nx][ny] != '1'):
                table[nx][ny] = node.deep + 1
                que.put(Node(nx, ny, node.deep + 1))
    return -1



datanum = 1000
datasize = 20

if __name__ == '__main__':
    f = open('data.txt', 'w')
    n, m = datanum, datanum
    print >>f, datasize
    cnt = 0
    for T in range(datasize + 20):
        A = numpy.random.randint((T + 1) * 2, size=(datanum, datanum))
        K = []
        startx, starty = random.randint(0, datanum - 1), random.randint(0, datanum - 1)
        endx, endy = random.randint(0, datanum - 1), random.randint(0, datanum - 1)
        if (startx == endx and starty == endy):
            continue
        cntx = 0
        cnty = 0
        for i in range(datanum):
            s = ''
            for j in range(datanum):
                if (i == startx and j == starty):
                    s += 'a'
                elif i == endx and j == endy:
                    s += 'b'
                elif A[i][j] <= (T + 1) * 2 - 2:
                    s += '0'
                    cntx += 1
                else:
                    s += '1'
                    cnty += 1
            K += [s]
        ans = EleTable(K, n, m) 
        print(cntx, cnty, ans)
        if (ans == -1):
            continue
        cnt += 1
        print >>f, n
        print >>f, m
        for i in range(n):
            print >>f, K[i]
        if cnt >= datasize:
            break
        
