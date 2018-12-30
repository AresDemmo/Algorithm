import random
import os

TSPFilename = 'algorithm_design_and_analysis/DeadWork/data/TSP.txt'
PackageFileName = 'algorithm_design_and_analysis/DeadWork/data/Package.txt'
EleTableFileName = 'algorithm_design_and_analysis/DeadWork/data/EleTable.txt'

dataNum = 100

def GegerateTSP():
    with open(TSPFilename, "w") as f:
        print(dataNum, file=f)
        for n in range(dataNum):
            print(n, file=f)
            for i in range(n):
                for j in range(n):
                    if i == j :
                        print(0, file=f)
                    else :
                        print(random.randint(0, 100), file=f)


def GeneratePackage():
    with open(PackageFileName, "w") as f:
        print(dataNum, file=f)
        for n in range(dataNum):
            print(n, file=f)
            print(n * random.randint(1, 5), file=f)
            for i in range(n):
                print(random.randint(1, 10), file=f)
                print(random.randint(1, 10), file=f)

def GenerateEleTable():
    pass

if __name__ == '__main__':
    GegerateTSP()
    GeneratePackage()
    GenerateEleTable()
