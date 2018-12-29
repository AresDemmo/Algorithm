
import Queue
import random

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

    def __cmp__(self,other):
        #call global(builtin) function cmp for int
        return cmp(self.CUB, other.CUB)

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
    for i in range(k + 1, N + 1):
        if rw < W[i]:
            pvu = pvl + rw * P[i] / W[i]
            for j in range(i + 1, N + 1):
                if rw > W[j]:
                    rw = rw - W[j]
                    pvl = pvl + P[j]
            return (pvl, pvu)
        rw = rw - W[i]
        pvl = pvl + P[i]
    pvu = pvl
    return (pvl, pvu)


def finish(answer, N):
    print "value = ", answer.CV
    id = answer.id
    while id != 0:
        if (tables[id].tag == 1):
            print tables[id].level
        id = tables[id].par


def DKpackage(W, P, N, M, e):
    (pvl, pvu) = LUBound(P, W, M, 0, N, 1)
    node = getNode(0, 0, 0, M, 0, pvu)
    prev = pvl - e
    que = Queue.PriorityQueue()
    que.put(node)
    while not que.empty():
        node = que.get()
        i = node.level + 1
        cap = node.CC
        cv = node.CV
        if node.CUB <= prev:
            break
        if i == N + 1:
            print cv, prev
            if cv > prev:
                prev = cv
                answer = node
        else:
            if cap > W[i]:
                cntnode = getNode(node.id, i, 1, cap - W[i], cv + P[i], node.CUB)
                que.put(cntnode)
            (pvl, pvu) = LUBound(P, W, cap, cv, N, i + 1)   
            if pvu > prev:
                cntnode = getNode(node.id, i, 0, cap, cv, pvl)  
                que.put(cntnode)      
    finish(answer, N) 
    return answer




if __name__ == '__main__':
    N = 20
    M = 50
    W = [0, 4, 6, 8, 3, 1, 1, 4, 5, 5, 7, 7, 8, 3, 7, 9, 9, 10, 8, 10, 6]
    P = [0, 1, 5, 1, 8, 4, 8, 7, 4, 6, 1, 4, 4, 5, 5, 7, 1, 8, 2, 7, 1]

    print W, sum(W)
    print P, sum(P)
    DKpackage(W, P, N, M, 0.01)