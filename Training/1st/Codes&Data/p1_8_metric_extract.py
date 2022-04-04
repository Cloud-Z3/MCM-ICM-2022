# Drawing heat map.

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import networkx as nx
import matplotlib
matplotlib.rcParams['font.sans-serif']=['Times New Roman']
#sns.set(style='whitegrid')
file1='2020_Problem_D_DATA'
file2='2020_Problem_D_DATA_After_Pro'
file3='Image'
file='passingevents_match1.csv'
p1='Problem1'
p2='Problem2'
p3='Problem3'
p4='Problem4'

fullevents=pd.read_csv(file1+'/'+'fullevents.csv')
#print(fullevents)
EventType=list(set(fullevents['EventType']))
print(EventType)
EventTypeCount=dict()
for event in EventType:
    EventTypeCount[event]=0
for i in fullevents.index:
    EventTypeCount[fullevents['EventType'][i]]+=1
EventType=[[EventTypeCount[event],event] for event in EventType]
for i in EventType:
    if i[1]=='Goalkeeper leaving line':
        i[1]='Goalkeeper\nleaving line'
    if i[1]=='Save attempt':
        i[1]='Save\nattempt'
    if i[1]=='Others on the ball':
        i[1]='Others\non the ball'
EventType.sort(reverse=True)
df=pd.DataFrame(EventType,columns=['Count','EventType'])
plt.figure(dpi=1000,figsize=(10,6))
sns.barplot(x='EventType',y='Count',data=df)
plt.savefig(file3+'/'+'p1_statistic.png')
#plt.show()
