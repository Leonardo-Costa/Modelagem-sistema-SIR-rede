from curses.ascii import SI
from turtle import right
import matplotlib.pyplot as plt
from tqdm import tqdm
import numpy as np
import networkx as nx


def GetGraph(graphSeed, N, M):
    G = nx.barabasi_albert_graph(n=N, m=M, seed=graphSeed, initial_graph=None)
    return G


def ShowData(result):
    plt.rcParams['figure.figsize'] = (10, 5)
    plt.xlabel('tempo')
    plt.ylabel('pessoas')
    value = ['S', 'I', 'R']
    for i in range(len(result)):
        plt.plot(result[i], label=value[i])
    print('maior número de infectados: {}'.format(max(result[1])))
    plt.legend()
    plt.show()


def GetMatrix(G, N):
    # retorna a matris de adjacencia de um grafo
    edges = list(G.edges())
    mtx = []
    for i in range(N):
        mtx.append([])
        for j in range(N):
            mtx[i].append([])
    if len(list(G.edges())) > 2:
        for i in range(len(list(G.edges()))):
            first = edges[i][0]
            scnd = edges[i][1]
            mtx[first][scnd] = 1
            mtx[scnd][first] = 1

        for i in range(len(mtx)):
            for j in range(len(mtx[i])):
                if mtx[i][j] != 1:
                    mtx[i][j] = 0
    else:
        mtx = [
            [[0], [1]],
            [[1], [0]]
        ]

    return mtx

def SetConnections(graphSeed, N, M):
    G = GetGraph(graphSeed, N, M)
    mtx = GetMatrix(G, N)
    return mtx
    

def MakeList(N):
    aux = []
    for i in range(N):
        aux.append([])
    return aux

def MakeChangeList(N):
    aux = []
    for i in range(N):
        aux.append(0)
    return aux


def Simulate(DT=0.01, Tmax=10000, S=1000, I=1, R=0, r=0.000002, a=0.001, showData=True, amostragem=100, graphSeed=10, N=10, M=2):
    
    SetConnections(graphSeed, N, M)

    SList = MakeList(N)
    IList = MakeList(N)
    RList = MakeList(N)

    S = MakeChangeList(N) 
    I = MakeChangeList(N)
    R = MakeChangeList(N)

    DS = MakeChangeList(N)
    DI = MakeChangeList(N)
    DR = MakeChangeList(N)

    iterations = int(Tmax / DT)

    for i in range(iterations):
        for j in range(N):
            DS[j] = DT * (-r * S[j] * I[j]) + M
            DI[j] = DT * (r * S[j] * I[j] - a * I[j])
            DR[j] = DT * (a * I[j])

            S[j] += DS[j]
            I[j] += DI[j]
            R[j] += DR[j]

            if i % amostragem == 0:
                SList.append(S[j])
                IList.append(I[j])
                RList.append(R[j])

    result = [SList, IList, RList]
    if showData:
        ShowData(result)
    else:
        return result
