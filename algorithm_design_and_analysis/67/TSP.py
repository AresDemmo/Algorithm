
class Solution:
    def __init__(self,X,start_node):
        self.X = X 
        self.start_node = start_node
        self.array = [[0]*(2**len(self.X)) for i in range(len(self.X))]

    def transfer(self,sets):
        su = 0
        for s in sets:
            su = su + 2**s
        return su

    def tsp(self):
        s = self.start_node
        num = len(self.X)
        cities = range(num)
        past_sets = [s] 
        cities.pop(cities.index(s))
        node = s
        return self.solve(node,cities)

    def solve(self,node,future_sets):
        if len(future_sets) == 0:
            return self.X[node][self.start_node]
        d = 99999
        distance = []
        for i in range(len(future_sets)):
            s_i = future_sets[i]
            copy = future_sets[:]
            copy.pop(i) 
            distance.append(self.X[node][s_i] + self.solve(s_i,copy))
        d = min(distance)
        next_one = future_sets[distance.index(d)]
        c = self.transfer(future_sets)
        self.array[node][c] = next_one

        return d

D = [[-1,20,30,10,11],[20,-1,16,4,2],[30,16,-1,6,7],[10,4,6,-1,12],[11,2,7,12,-1]]
S = Solution(D,0)

print(S.tsp())
M = S.array
lists = range(len(S.X))
start = S.start_node
while len(lists) > 0:
    lists.pop(lists.index(start))

    m = S.transfer(lists)

    next_node = S.array[start][m]

    print(start,"--->" ,next_node)

    start = next_node
