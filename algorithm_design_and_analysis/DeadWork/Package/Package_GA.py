from queue import PriorityQueue
import random
import math
import datetime
import numpy
import copy


inFilename = 'algorithm_design_and_analysis/DeadWork/data/Package.txt'
outFilename = 'algorithm_design_and_analysis/DeadWork/Output/Package_GA.txt'
        
class Node(object):
    def __init__(self, chrom, weight, fitness, parent1, parent2, cross):
        self.chrom = copy.deepcopy(chrom)
        self.weight = weight
        self.fitness = fitness
        self.parent1 = parent1
        self.parent2 = parent2
        self.cross = cross

popsize = 200 #种群规模
pc = 0.618 #交配概率
pm = 0.03 #变异概率
mut_NUm = 0 # 每次变异个数
maxgen = 100 #最大进化代数

#global variable
n, C = 0, 0
sumfitness, minfitness, maxfitness, avgfitness = 0, 0, 0, 0
minpop, maxpop = 0, 0
oldpop = []
newpop = []
W = P = []
proStrong1to0 = 0.8 #在空间数很小的时候，通过随机很难找到一个初始解，通过强硬的转变，直接剪掉一些物品的选择


#计算当前选择的物品的占用空间
def cal_weight(s):
    pop_weight = 0
    for j in range(n):
        pop_weight += s[j] * W[j]
    return pop_weight

#计算当前选择物品的总价值
def cal_fit(s):
    pop_fit = 0
    for j in range(n):
        pop_fit += s[j] * P[j]
    return pop_fit

#产生初始种群
def initpop():
    global oldpop, newpop
    oldpop, newpop = [], []
    for i in range(popsize):
        ispop = False
        chrom = numpy.random.randint(0, 2, size=(n))
        while(not ispop):
            tempweight = cal_weight(chrom)
            if (tempweight <= C):
                oldpop += [Node(chrom, tempweight, cal_fit(chrom), 0, 0, 0)]
                ispop = True
            else :
                for i in range(len(chrom)):
                    if chrom[i] == 1 and execise(proStrong1to0):
                        chrom[i] = 0
                ispop = False
    newpop = copy.deepcopy(oldpop)
    
#统计适用性信息，适用性最大的和适用性最小的
def statistics(pop):
    global sumfitness, minfitness, maxfitness, avgfitness, maxpop, minpop
    sumfitness = 0
    minfitness = maxfitness = pop[0].fitness
    maxpop = minpop = 0
    for i in range(popsize):
        sumfitness += pop[i].fitness
        tmpfit = pop[i].fitness
        if (tmpfit > maxfitness):
            maxfitness = pop[i].fitness
            maxpop = i
        if (tmpfit < minfitness):
            minfitness = pop[i].fitness
            minpop = i
    avgfitness = 1.0 * sumfitness / popsize


#选择，轮转法
def selection():
    rand_Number = random.randint(0, 2000) / 2000.0
    wheel_pos = rand_Number * sumfitness
    partsum = parent = 0
    while True:
        partsum += oldpop[parent].fitness
        parent += 1
        if (partsum < wheel_pos or parent < popsize):
            break
    return parent - 1

#概率选择实验
def execise(probability):
    pp = random.randint(0, 200000) / 200000.0
    if pp <= probability:
        return False
    return True

#产生交配群落
#par1 111 101
#par2 111 010
#pos = 3
#new 111 010
def crossover(parent1, parent2, i):
    if execise(pc):
        cross_pos = random.randint(0, n - 2)
    else:
        cross_pos = n - 1

    for j in range(cross_pos + 1):
        newpop[i].chrom[j] = parent1[j]
    for j in range(cross_pos + 1, n):
        newpop[i].chrom[j] = parent2[j]
    newpop[i].cross = cross_pos
    return True


#产生变异群落
def mutation(alleles):
    if (execise(pm)):
        if (alleles == 1):
            alleles = 0
        else:
            alleles = 1
    return alleles

#产生新一代种群
def generation():
    global newpop, oldpop
    i = 0
    id = 0
    while(i < popsize):
        ispop = False
        mate1 = selection()
        mate2 = selection()
        crossover(oldpop[mate1].chrom, oldpop[mate2].chrom, i)
        while(not ispop):
            id += 1

            #每次固定改变mut_NUm个，加快速度
            for cnt_k in range(mut_NUm):
                rand_Mut = random.randint(0, n - 1)
                newpop[i].chrom[rand_Mut] = 1 - newpop[i].chrom[rand_Mut]
            
            tmpweight = cal_weight(newpop[i].chrom)
            if (tmpweight <= C):
                newpop[i].fitness = cal_fit(newpop[i].chrom)
                newpop[i].weight = tmpweight
                newpop[i].parent1 = mate1
                newpop[i].parent2 = mate2
                ispop = True
            else:
                for cnt in range(len(newpop[i].chrom)):
                    if newpop[i].chrom[cnt] == 1 and execise(proStrong1to0):
                        newpop[i].chrom[cnt] = 0
                ispop = False
        i += 1
    
    # print('generate = ', id)


def Package_GA():
    global newpop, oldpop
    if (n == 0):
        return 0
    initpop()
    statistics(newpop)
    gen = 0 
    while(gen < maxgen):
        gen = gen + 1
        oldmax = maxfitness
        oldmaxpop = maxpop
        generation()
        statistics(newpop)
        if (maxfitness < oldmax):
            newpop[minpop] = copy.deepcopy(oldpop[oldmaxpop])
            statistics(newpop)

        #直接换引用，加快速度
        t = oldpop
        oldpop = newpop
        newpop = t

    return maxfitness

class Pair(object):
    def __init__(self, w, p):
        self.w = w
        self.p = p
    def __lt__(self, Other):
        return 1.0 * self.p / self.w > 1.0 * Other.p / Other.w

if __name__ == '__main__':
    outf = open(outFilename, "w")
    with open(inFilename) as data:
        T = int(data.readline())
        for i in range(T):
            n = int(data.readline())
            C = int(data.readline())
            
            W, P = [], []

            for i in range(n):
                W += [int(data.readline())]
                P += [int(data.readline())]
            if (n == 0):
                continue

            sum_W = sum(W)
            proStrong1to0 = 1.0 - 1.0 * C / sum_W
            pm = 1.0 / n
            mut_NUm = int(sum_W / C * 2)


            starttime = datetime.datetime.now()
            value = Package_GA()
            endtime = datetime.datetime.now()
            time = (endtime - starttime).seconds
            print(n, time, value, file=outf)
            print(n, time, value)