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


df=pd.read_csv("./data/influence_data.csv")
influencer=df['influencer_name']
follower=df['follower_name']
print(df)

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
