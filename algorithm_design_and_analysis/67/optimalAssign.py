import Queue
import random

class Node(object):
    def __init__(self, cost, state, level):
        self.cost = cost
        self.state = state
        self.level = level

    def __lt__(self, other):#operator < 
        return self.cost < other.cost

    def __cmp__(self,other):
        #call global(builtin) function cmp for int
        return cmp(self.cost, other.cost)

    def __str__(self):
        return (self.cost, self.state, self.level)

def optimalAssign(n, k, t):
    answer = sum(t)
    que = Queue.PriorityQueue()
    que.put(Node(0, [0 for i in range(k)], 0))
    while not que.empty():
        node = que.get()
        (cost, state, level) = (node.cost, node.state, node.level)
        if level == n:
            answer = min(answer, cost)
            continue
        #downbound(cost, level)
        if cost > answer:
            continue
        for i in range(k):   
            c = max(cost, state[i] + t[level])
            s = state[:]
            s[i] += t[level]
            que.put(Node(c, s, level + 1))
    return answer

if __name__ == '__main__':
    n = 10
    k = 3
    t = [random.randint(1, 10) for i in range(n)]
    print t
    print optimalAssign(n, k, t)