import pandas as pd

def qua(nums):
    nums.sort()
    n=len(nums)
    a=nums[0]
    i=n//5
    return [a+i,a+i*2,a+i*3,a+i*4]

def allocate(sep,value):
    a,b,c,d=sep
    if value<=a:
        return 'A'
    elif value<=b:
        return 'B'
    elif value<=c:
        return 'C'
    elif value<=d:
        return 'D'
    else:
        return 'E'

def process(df,file1,file2):
    influencer=df['influencer_name']
    follower=df['follower_name']
    #print(df)

    musician=set(df['influencer_name'])|set(df['follower_name'])
    musician=list(musician)
    #print(musician)
    mu_id=dict()
    for i,m in enumerate(musician):
        mu_id[m]=i

    n=len(musician)
    adj=[[0 for _ in range(n)] for _ in range(n)]

    for i in df.index:
        a,b=mu_id[influencer[i]],mu_id[follower[i]]
        adj[a][b]+=1
    #print(adj)

    matrix=[]
    for i in range(n):
        for j in range(n):
            if adj[i][j]!=0:
                matrix.append([i,j,adj[i][j]])

    # 选择具有影响力的音乐家、深受影响的音乐家
    threshold=0
    musician_new=set(musician)
    for i in range(n):
        if sum(adj[i])<threshold and sum([adj[j][i] for j in range(n)])<threshold:
            musician_new.remove(musician[i])

    musician_new=list(musician_new)
    n_=len(musician_new)
    adj_=[[0 for _ in range(n_)] for _ in range(n_)]
    mu_id_=dict()
    for i,m in enumerate(musician_new):
        mu_id_[m]=i
    for i in df.index:
        if influencer[i] in musician_new and follower[i] in musician_new:
            a,b=mu_id_[influencer[i]],mu_id_[follower[i]]
            adj_[a][b]+=1
    #print(adj_)

    matrix_=[]
    Id=0
    for i in range(n_):
        for j in range(n_):
            if adj_[i][j]!=0:
                matrix_.append([i,j,'Directed',Id,adj_[i][j]])
                Id+=1

    df_out=pd.DataFrame(data=matrix_,columns=['Source','Target','Type','Id','Weight'])
    df_out.to_csv(file2,index=False)
    # 边

    matrix_=[]
    sep=qua([sum(adj_[i]) for i in range(n_)])
    for i in range(n_):
        weight=sum(adj_[i])
        matrix_.append([i,musician_new[i],weight,allocate(sep,weight)])
    df_out=pd.DataFrame(data=matrix_,columns=['Id','Label','Weight','color'])
    # 节点
    df_out.to_csv(file1,index=False)

def process2(df,file1,file2):
    influencer = df['influencer_name']
    follower = df['follower_name']
    #print(df)

    musician=[]
    for i in df.index:
        if influencer[i] not in musician:
            musician.append(influencer[i])
        if follower[i] not in musician:
            musician.append(follower[i])
    # print(musician)
    mu_id = dict()
    for i, m in enumerate(musician):
        mu_id[m] = i

    n = len(musician)
    adj = [[0 for _ in range(n)] for _ in range(n)]

    for i in df.index:
        a, b = mu_id[influencer[i]], mu_id[follower[i]]
        adj[a][b] += 1
    # print(adj)

    matrix = []
    for i in range(n):
        for j in range(n):
            if adj[i][j] != 0:
                matrix.append([i, j, adj[i][j]])

    # 选择具有影响力的音乐家、深受影响的音乐家
    threshold = 0
    musician_new = set(musician)
    for i in range(n):
        if sum(adj[i]) < threshold and sum([adj[j][i] for j in range(n)]) < threshold:
            musician_new.remove(musician[i])

    musician_new = list(musician_new)
    n_ = len(musician_new)
    adj_ = [[0 for _ in range(n_)] for _ in range(n_)]
    mu_id_ = dict()
    for i, m in enumerate(musician_new):
        mu_id_[m] = i
    for i in df.index:
        if influencer[i] in musician_new and follower[i] in musician_new:
            a, b = mu_id_[influencer[i]], mu_id_[follower[i]]
            adj_[a][b] += 1
    #print(adj_)

    matrix_ = []
    Id = 0
    for i in range(n_):
        for j in range(n_):
            if adj_[i][j] != 0:
                matrix_.append([i, j, 'Directed', Id, adj_[i][j]])
                Id += 1

    df_out = pd.DataFrame(data=matrix_, columns=['Source', 'Target', 'Type', 'Id', 'Weight'])
    df_out.to_csv(file2,index=False)
    # 边

    matrix_ = []
    sep = qua([sum(adj_[i]) for i in range(n_)])
    for i in range(n_):
        weight = sum(adj_[i])
        matrix_.append([i, musician_new[i], weight, allocate(sep, weight)])
    df_out = pd.DataFrame(data=matrix_, columns=['Id', 'Label', 'Weight', 'color'])
    # 节点
    df_out.to_csv(file1, index=False)


