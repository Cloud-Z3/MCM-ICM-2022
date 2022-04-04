import pandas as pd
import numpy as np
from collections import Counter
import os
from Q1_lib import *

files=os.listdir('./Data/p1/subnet_data')
files.sort()
df=pd.read_csv('./data/influence_data.csv')
influencer=df['influencer_name']
follower=df['follower_name']
for file in files:
    df_sub=pd.read_csv('./Data/p1/subnet_data/'+file)
    musician=set(df_sub['Label'])
    print(file)
    line=[]
    for i in df.index:
        if influencer[i] in musician and follower[i] in musician:
            line.append(i)
    if not line:continue
    df_community=df.loc[line]
    print(df_community)
    file1=f'./Data/p1/subnet_edge&data/nodes_{file}'
    file2=f'./Data/p1/subnet_edge&data/edges_{file}'
    process(df_community,file1,file2)


