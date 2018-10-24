
import EuclideanDistance
import DivergenceDistance

def main():
    A = [[1, 0, 0],[0, 1, 0],[0, 0, 1]]
    B = [[1, 0, 0],[0, 1, 0],[1, 1, 1]]
    print EuclideanDistance.EucliDistance(A,B)
    print DivergenceDistance.Distance(A,B)
if __name__ == '__main__':
    main()
