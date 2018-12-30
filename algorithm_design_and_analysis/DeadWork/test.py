import copy

class Node(object):
    def __init__(self, length, path):
        self.length = length
        self.path = copy.deepcopy(path)

    def copy(self, length, path):
        self.length = length
        self.path = copy.deepcopy(path)

n = 0

def haha():
    print(n)

if __name__ == '__main__':
    n = 10
    haha()