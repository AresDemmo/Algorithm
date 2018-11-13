import Queue

class Node(object):
    def __init__(self, value, state, level):
        self.value = value
        self.state = state
        self.level = level

    def __lt__(self, other):#operator < 
        return self.value < other.value

    def __cmp__(self,other):
        #call global(builtin) function cmp for int
        return cmp(self.value, other.value)

    def __str__(self):
        return (self.value, self.state, self.level)



def assignWork(C, n):
    answer = 77777777
    que = Queue.PriorityQueue()
    que.put(Node(0, 0, 0))
    while not que.empty():
        node = que.get()
        (value, state, level) = (node.value, node.state, node.level)
        if level == n:
            answer = min(answer, value)
            continue
        if value > answer:
            continue
        for i in range(n):
            k = (1 << i)
            if state & k == 0:
                que.put(Node(value + C[level][i], state | k, level + 1))
    return answer
    

if __name__ == '__main__':
    C = [[1, 2, 3, 4], [2, 3, 2, 3], [3, 2, 4, 1], [4, 3, 1, 2]]
    print assignWork(C, 4)