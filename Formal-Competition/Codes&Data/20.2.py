import math
import copy
import numpy as np
from scipy.stats import zscore
# from maturity_2 import *

def maturaty(people,technologies,processes):
    n1=len(people)
    n2=len(technologies)
    n3=len(processes)
    w=[0.2557,0.0764,0.5305,0.1374]
    Q_average=Quality(people,n1)
    P_average=Performance(people,n1)
    num1=len(Q_average)
    peo=[]
    for i in range(num1):
        peo.append(w[0]*Q_average[i]+w[1]*P_average[i]+w[2]*people[i][-2]+w[3]*people[i][-1])
    tec=tech(technologies,n2)
    pro=proc(processes,n3)
    return peo,tec,pro

def Quality(people1,n1):
    Q_average=-1
    people=copy.deepcopy(people1)
    ans1=[]
    for i in range(n1):
        for m in range(4):
            sum1=0
            for j in range(len(people[i])-2):
                sum1+=people[i][j][m]
            for j in range(len(people[i])-2):
                people[i][j][m]=people[i][j][m]/sum1
        list1=[]
        for m in range(4):
            sum2=0
            for k in range(len(people[i])-2):
                sum2+=(-people[i][k][m])*math.log(people[i][k][m])
            list1.append(sum2)
        list2=[]
        for q in range(4):
            list2.append(list1[q]/sum(list1))
        list3=[]
        for q in range(len(people[i])-2):
            sum3=0
            for k in range(4):
                sum3+=people1[i][q][k]*list2[k]
            list3.append(sum3)
        Q_average=sum(list3)/len(list3)
        ans1.append(Q_average)
    return ans1

def Performance(people1,n1):
    P_average = -1
    people = copy.deepcopy(people1)
    ans1=[]
    for i in range(n1):
        for m in range(4,7):
            sum1 = 0
            for j in range(len(people[i]) - 2):
                sum1 += people[i][j][m]
            for j in range(len(people[i]) - 2):
                people[i][j][m] = people[i][j][m] / sum1
        list1 = []
        for m in range(4,7):
            sum2 = 0
            for k in range(len(people[i]) - 2):
                sum2 += (-people[i][k][m]) * math.log(people[i][k][m])
            list1.append(sum2)
        list2 = []
        for q in range(3):
            list2.append(list1[q] / sum(list1))
        list3 = []
        for q in range(len(people[i]) - 2):
            sum3 = 0
            for k in range(4,7):
                sum3 += people1[i][q][k] * list2[k-4]
            list3.append(sum3)
        P_average = sum(list3) / len(list3)
        ans1.append(P_average)
    return ans1

def tech(technologies,n2):
    w1=0.1836
    w2=0.281
    w3=0.0388
    w4=0.1068
    w5=0.3898
    w=[w1,w2,w3,w4,w5]
    list1=[]
    for i in range(n2):
        sum1=0
        for j in range(5):
            sum1+=technologies[i][j]*w[j]
        list1.append(sum1)
    return list1

def proc(processes,n3):
    w1=0.1142
    w2=0.3236
    w3=0.1796
    w4=0.2820
    w5=0.0362
    w6=0.0644
    w=[w1,w2,w3,w4,w5,w6]
    list1=[]
    for i in range(n3):
        sum1=0
        for j in range(6):
            sum1+=processes[i][j]*w[j]
        list1.append(sum1)
    return list1

def mutiplevalue(people,technologies,processes):
    peo,tec,pro=maturaty(people,technologies,processes)
    matrix = []
    for i in range(len(peo)):
        p1,t,p2=peo[i],tec[i],pro[i]
        matrix.append([p1,t,p2,p1*t,p1*p2,t*p2,p1*t*p2])
    return PCA(matrix)

def PCA(matrix):
    can=matrix[-1].copy()
    a=np.array(matrix)
    b=a
    c = zscore(b)   # gj
    print(len(c),len(c[0]))
    r = np.corrcoef(c.T)  # 数据标准化并计算相关系数阵
    d, e = np.linalg.eig(r)  # 求特征值和特征向量
    d_id=[[d[i],i] for i in range(len(e))]
    d_id.sort(reverse=True)
    d,did=zip(*d_id)
    enew=[]
    for i in range(len(e)):
        enew.append([e[i][did[j]] for j in range(len(e))])
    e=np.array(enew)
    s=sum(d)
    rate=[di/s for di in d]
    n=len(e)
    f=[[1 if sum([e[j][i] for j in range(n)])>=0 else -1 for i in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            e[i][j]=e[i][j]*f[i][j]
    k=1
    s=rate[0]
    while s<0.9:
        s+=rate[k]
        k+=1
    print(k)
    print(rate)
    F = e[:, :k]
    print(F)
    score_mat = c.dot(F)  # 计算主成分得分矩阵   df
    score1 = score_mat.dot(rate[0:k])  # 计算各评价对象的得分 tf
    score2 = -score1  # 通过表中数据以及score1观测，需要调整得分的正负号
    # print("各评价对象的得分为：", score2)
    index = score2.argsort()   # 排序后的每个元素在原数组中的位置
    weight=[sum([rate[j]*e[i][j] for j in range(k)]) for i in range(7)]
    s=sum(weight)
    rate=[w/s for w in weight]
    print(rate)
    return sum([can[i]*rate[i] for i in range(len(rate))])

def read(file1,file2,file3):
    people=[]
    technologies=[]
    processes=[]
    with open(file1) as f:
        while True:
            pt=f.readline()
            if pt=='':
                break
            else:
                p=[]
                pt=list(map(float,pt.split()))
                id1,id2=0,6
                while id2<len(pt):
                    p.append(pt[id1:id2+1])
                    id1+=7
                    id2+=7
                p.append(pt[-2])
                p.append(pt[-1])
                people.append(p)
    with open(file2) as f:
        while True:
            tt=f.readline()
            if tt=='':
                break
            else:
                tt=list(map(float,tt.split()))
                technologies.append(tt)
    with open(file3) as f:
        while True:
            pt=f.readline()
            if pt=='':
                break
            else:
                pt=list(map(float,pt.split()))
                processes.append(pt)
    return people,technologies,processes

# people=[
#     [[1,2,3,4,5,6,7],[7,6,5,4,3,2,1],[1,2,3,4,5,6,7],4,5], # 员工1，员工2，员工3，指标4，指标5
#     [[1,2,3,4,5,6,7],[7,6,5,4,3,2,1],[1,2,3,4,5,6,7],4,5],
#     [[1,2,3,4,5,6,7],[7,6,5,4,3,2,1],[1,2,3,4,5,6,7],4,5],
#     [[1,2,3,4,5,6,7],[7,6,5,4,3,2,1],[1,2,3,4,5,6,7],4,5],
#     [[1,2,3,4,5,6,7],[7,6,5,4,3,2,1],[1,2,3,4,5,6,7],4,5],
#     [[1,2,3,4,5,6,7],[7,6,5,4,3,2,1],[1,2,3,4,5,6,7],4,5],
#     [[1,2,3,4,5,6,7],[7,6,5,4,3,2,1],4,5]
#     ]
# technologies=[
#     [1,2,3,4,5], # 5个指标
#     [1,2,3,4,5],
#     [1,2,3,4,5],
#     [1,2,3,4,5],
#     [1,2,3,4,5],
#     [1,2,3,4,5],
#     [1,2,3,4,8]
#     ]
# processes=[[1,2,3,4,5,6] for _ in range(7)] # 6个指标
people,technologies,processes=read('./p2/people.txt','./p2/technologies.txt','./p2/processes.txt')
print(mutiplevalue(people,technologies,processes))
