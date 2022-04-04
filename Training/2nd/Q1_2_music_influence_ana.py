import pandas as pd
import numpy as np


df=pd.read_csv("./Data/p1/6_music_influence.csv")
print(df['Weight'])
print(max(df['Weight']))
weight=[[df['Weight'][i],i] for i in df.index]
weight.sort(reverse=True)
for i in range(20):
    print(df['Label'][weight[i][1]],weight[i][0])


