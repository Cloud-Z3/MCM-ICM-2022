import numpy as np
from scipy.stats import zscore

def PCA(matrix):
    a=np.array(matrix)
    b=a
    c = zscore(b)   # gj
    print(c)
    r = np.corrcoef(c.T)  # 数据标准化并计算相关系数阵
    d, e = np.linalg.eig(r)  # 求特征值和特征向量
    d_id=[[d[i],i] for i in range(len(e))]
    d_id.sort(reverse=True)
    d,did=zip(*d_id)
    enew=[]
    for i in range(len(e)):
        enew.append([e[i][did[j]] for j in range(len(e))])
    e=np.array(enew)
    print(e)
    s=sum(d)
    rate=[di/s for di in d]
    n=len(e)
    f=[[1 if sum([e[j][i] for j in range(n)])>=0 else -1 for i in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            e[i][j]=e[i][j]*f[i][j]

    k = 5  # 提出主成分的个数
    F = e[:, :k]
    score_mat = c.dot(F)  # 计算主成分得分矩阵   df
    score1 = score_mat.dot(rate[0:k])  # 计算各评价对象的得分 tf
    score2 = -score1  # 通过表中数据以及score1观测，需要调整得分的正负号
    # print("各评价对象的得分为：", score2)
    index = score2.argsort()   # 排序后的每个元素在原数组中的位置
    return score1[max(index)]

