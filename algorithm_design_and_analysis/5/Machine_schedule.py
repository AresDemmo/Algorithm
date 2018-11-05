
import numpy

def MachineSchedule(A, B, n):
    k = min(sum(A), sum(B))
    dp = numpy.zeros((k + 1, n + 1), dtype=int)
    
    pass


if __name__ == '__main__':
    A = [2, 5, 7, 10, 5, 2]
    B = [3, 8, 4, 11, 3, 4]
    n = len(A)
    MachineSchedule(A, B, n)