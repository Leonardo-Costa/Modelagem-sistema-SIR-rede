import matplotlib.pyplot as plt
from tqdm import tqdm
import numpy as np

def ShowData(result, num):
    for i in range(len(result[0])):
        plt.rcParams['figure.figsize'] = (10, 5)
        plt.xlabel('tempo')
        plt.ylabel('Infectados')
        value = ['S', 'I', 'R']
        for j in range(len(result)):
            plt.plot(result[1][i], color=(1-i/9,i/9,0))
        print('maior número de infectados: {}'.format(max(result[1][i])))
    plt.legend()
    plt.savefig(fname='simulação-{}'.format(num + 1))  

def MakeList(N):
    aux = []
    for i in range(N):
        aux.append([])
    return aux

def MakeChangeList(N, initialValue = 0):
    aux = []
    for i in range(N):
        aux.append(initialValue)
    return aux


def Simulate(DT=0.01, Tmax=20000, S=1000, I=1, R=0, r=0.000002, a=0.001, showData=True, amostragem=100, N=4, num=0):
    
    SList = MakeList(N)
    IList = MakeList(N)
    RList = MakeList(N)

    S = MakeChangeList(N, 2000) 
    I = MakeChangeList(N, 0)
    R = MakeChangeList(N, 0) 
    DS = MakeChangeList(N)
    DI = MakeChangeList(N)
    DR = MakeChangeList(N) 

    I[0] = 10

    for i in tqdm(range(int(Tmax / DT))):
        for j in range(N):
            DS[j] = DT * (-r * S[j] * I[j])
            DI[j] = DT * (r * S[j] * I[j] - a * I[j])
            DR[j] = DT * (a * I[j])

            S[j] += DS[j]
            I[j] += DI[j]
            R[j] += DR[j]
# 1000 simulacao 1
# 10000 simulacao 2
# 100000 simulacao 3
# 1000000 simulacao 4
# 100000000 simulacao 5
            aux = I[j-1] / (1000 * 10 ** num)
            I[j] += aux
            I[j-1] -= aux
            
            if i % amostragem == 0:
                SList[j].append(S[j])
                IList[j].append(I[j])
                RList[j].append(R[j])

    result = [SList, IList, RList]
    if showData:
        ShowData(result, num)
    else:
        return result
