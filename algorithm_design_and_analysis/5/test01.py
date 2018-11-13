

def getMaxValueOfPackage(N, C, W, V):

    cell = [[0 for i in range(C+1)] for j in range(N+1)]

    for i in range(1, N+1):

        for j in range(1, C+1):

            cell[i][j] = cell[i-1][j]

            if j >= W[i-1] and cell[i][j] < V[i-1] + cell[i-1][j-W[i-1]]:

                cell[i][j] = V[i-1] + cell[i-1][j-W[i-1]]

    for i in range(N+1):

        print cell[i]

    return cell


def show(N, C, W, Cell, Goods):

    print 'value:', Cell[N][C]

    processed = [False for i in range(N)]

    cap = C

    for i in range(N, 0, -1):

        if Cell[i][cap] != Cell[i-1][cap]:

            processed[i-1] = True

            cap -= W[i-1]

    print 'choose:'

    for i in range(N):

        if processed[i]:
            print i
    print 'cap:',cap


if __name__ == "__main__":
    goods_types = 20
    capacity = 50
    W = [4, 6, 8, 3, 1, 1, 4, 5, 5, 7, 7, 8, 3, 7, 9, 9, 10, 8, 10, 6]
    P = [1, 5, 1, 8, 4, 8, 7, 4, 6, 1, 4, 4, 5, 5, 7, 1, 8, 2, 7, 1]
    cc = getMaxValueOfPackage(goods_types, capacity, W, P)

    show(goods_types, capacity, W, cc, P)
