import random
import os

TSPFilename = 'algorithm_design_and_analysis/DeadWork/data/TSP'
PackageFileName = 'algorithm_design_and_analysis/DeadWork/data/Package'
EleTableFileName = 'algorithm_design_and_analysis/DeadWork/data/EleTable'

def GegerateTSP(n):
    f = open(TSPFilename + "/" + n + ".txt", "w")
    print("haha", file=f)

def GeneratePackage(n):
    pass

def GenerateEleTable(n):
    pass

if __name__ == '__main':
    A = [20, 30, 50, 100]
    for i in A:
        GegerateTSP(i)
        GeneratePackage(i)
        GenerateEleTable(i)
