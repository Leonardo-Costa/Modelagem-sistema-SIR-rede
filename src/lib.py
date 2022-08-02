import matplotlib.pyplot as plt
from tqdm import tqdm
import numpy as np

def ShowData(result):
    for i in range(len(result[0])):
        plt.rcParams['figure.figsize'] = (10, 5)
        plt.xlabel('tempo')
        plt.ylabel('pessoas')
        value = ['S', 'I', 'R']
        for j in range(len(result)):
            plt.plot(result[j][i], label=value[j])
        print('maior número de infectados: {}'.format(max(result[1][i])))
        plt.legend()
        plt.show()    

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


def Simulate(DT=0.01, Tmax=20000, S=1000, I=1, R=0, r=0.000002, a=0.001, showData=True, amostragem=100, N=2):
    
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

            
            if i % amostragem == 0:
                SList[j].append(S[j])
                IList[j].append(I[j])
                RList[j].append(R[j])

    result = [SList, IList, RList]
    if showData:
        ShowData(result)
    else:
        return result
