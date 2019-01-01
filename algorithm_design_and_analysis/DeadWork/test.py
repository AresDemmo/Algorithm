import numpy
import os
import datetime
from queue import PriorityQueue
import copy


class Node(object):
    def __init__(self, cost):
        self.cost = cost
    def __lt__(self, other):#operator < 
        return self.cost < other.cost
    def __cmp__(self,other):
        #call global(builtin) function cmp for int
        return self.cost > self.cost

if __name__ == '__main__':
    que = PriorityQueue()
    que.put(Node(1))
    que.put(Node(5))
    que.put(Node(2))
    while not que.empty():
        node = que.get()
        print(node.cost)
    
    