# this is a algorithm of Non-negative Matrix Factorization
# refrence : Daniel D. Lee and H. Sebastian Seung: Algorithms 
#            for Non-negative Matrix Factorization.


import DivergenceDistance
import EuclideanDistance
import random

#fuck windows, numpy can't install, programing matrix algothrim by myself

def randomMatrix(h, w):
    return [[random.random() for i in range(w)] for j in range(h)]

def zeroMatrix(h, w):
    return [[0 for i in range(w)] for j in range(h)]
    
def transMatrix(A):
    return [[A[i][j] for i in range(len(A))] for j in range(len(A[0]))]


def MatrixMul(A, B):
    if len(A[0]) != len(B):
        return 'false : the length of A , b not feasible' 
    C = zeroMatrix(len(A), len(B[0]))
    for i in range(len(A)):
        for j in range(len(B[0])):
            for k in range(len(A[0])):
                C[i][j] += A[i][k] * B[k][j]
    return C


#fuck over


def EucDis(V, r, iterator):
    H = randomMatrix(r, len(V[0]))
    W = randomMatrix(len(V), r)
    Dis = []
    for i in range(iterator):
        
        A = MatrixMul(transMatrix(W), V)
        B = MatrixMul(MatrixMul(transMatrix(W), W), H)

        "update H"
        for a in range(r):
            for b in range(len(V[0])):
                H[a][b] = H[a][b] * A[a][b] / B[a][b]
        
        C = MatrixMul(V, transMatrix(H))
        D = MatrixMul(W, MatrixMul(H, transMatrix(H)))
                        
        "update W"
        for a in range(len(V)):
            for b in range(r):
                W[a][b] = W[a][b] * C[a][b] / D[a][b]

        Ori = MatrixMul(W, H)
        Dis += [EuclideanDistance.EucliDistance(V, Ori)]
    return (H, W, Dis)


def DivDis(V, r, iterator):
    H = randomMatrix(r, len(V[0]))
    W = randomMatrix(len(V), r)
    Dis = []
    for i in range(iterator):
        Ori = MatrixMul(W, H)
        "update H"
        for a in range(r):
            for b in range(len(V[0])):
                suma = 0
                sumb = 0
                for c in range(len(V)):
                    suma += W[c][a] * V[c][b] / Ori[c][b]
                    sumb += W[c][a]
                H[a][b] = H[a][b] * suma / sumb
        
        Ori = MatrixMul(W, H)            
        "update W"
        for a in range(len(V)):
            for b in range(r):
                suma = 0
                sumb = 0
                for c in range(len(V)):
                    suma += H[b][c] * V[a][c] / Ori[a][c]
                    sumb += H[b][c]
                W[a][b] = W[a][b] * suma / sumb

        Ori = MatrixMul(W, H)
        Dis += [EuclideanDistance.EucliDistance(V, Ori)]
        
    return (H, W, Dis)          
    
def NMF(V, r = 3, iterator=10, algorithm=EucDis):
    return algorithm(V, r, iterator)


if __name__ == '__main__':

    A = randomMatrix(4, 4)
    [H, W, Dis] = NMF(A, 2, iterator=100)
    [H, W, Dis2] = NMF(A, 2, iterator=100, algorithm=DivDis)
    
    x = [i for i in range(100)]
    for i in range(1, 100, 1):
        if (Dis[i] > Dis[i - 1]): print "Fail EucDis", i
    for i in range(1, 100, 1):
        if (Dis[i] > Dis2[i - 1]): print "Fail DivDis", i
    import pylab
    pylab.plot(x, Dis, label='EucDis')
    pylab.plot(x, Dis2, label='DivDis')
    pylab.legend(loc='upper left')
    pylab.show()
    #pylab.savefig('Net_Data_Mining_Task_Reading\\image\\Correct_answer.png')

