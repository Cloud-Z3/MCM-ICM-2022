import pandas as pd
import numpy as np
from collections import Counter

df=pd.read_csv("./Data/p1/6_community_mwbased.csv")
counter=Counter(df['modularity_class'])
print(counter)
can=[]
for i in counter:
    if 10<=counter[i]<=40:
        can.append(i)
print(can)
#print(abc)
for i,c in enumerate(can):
    line=[]
    for idx in df.index:
        if df['modularity_class'][idx]==c:
            line.append(idx)
    df_out=df.loc[line]
    #df_out.to_csv(f"./Data/p1/subnet_data/subnet{str(i)}.csv",index=False)

