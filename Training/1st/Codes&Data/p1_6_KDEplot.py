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
fulleventsnew=fullevents.copy()
fulleventsnew['Event_x']=(fulleventsnew['EventOrigin_x']+fulleventsnew['EventDestination_x'])/2
fulleventsnew['Event_y']=(fulleventsnew['EventOrigin_y']+fulleventsnew['EventDestination_y'])/2
fulleventsnew.to_csv(file2+'/'+p1+'/'+'fulleventsnew.csv')

#sns.kdeplot(data=fullevents,x="X",y="Y",fill=True)
#plt.show()

fullevents=pd.read_csv(file2+'/'+p1+'/'+'fullevents.csv')
print(fullevents)
EventType=list(set(fullevents['EventType']))
print(EventType)

'''
#KDE，绘制热力图
for i,item in enumerate(EventType):
    plt.figure(dpi=400,figsize=(5,2.5))
    plt.xlim(-20,120)
    plt.ylim(-20,120)
    data=fullevents[fullevents['EventType']==item]
    print(i,item)
    sns.kdeplot(data=data,x="Event_x",y="Event_y",fill=True)
    #img = plt.imread(file1 + '/' + '15.2.3.png')
    #ax.imshow(img, extent=[0, 100, 0, 100])
    #plt.show()
    plt.savefig(file3+'/'+'p1_'+str(i)+'_'+item+'_.png')
    plt.close()'''
for i,item in enumerate(EventType):
    plt.figure(dpi=400,figsize=(5,2.5))
    plt.xlim(-20,120)
    plt.ylim(-20,120)
    data=fullevents[fullevents['EventType']==item]
    print(i,item)
    sns.scatterplot(data=data,x="EventDestination_x",y="EventDestination_y")
    #img = plt.imread(file1 + '/' + '15.2.3.png')
    #ax.imshow(img, extent=[0, 100, 0, 100])
    #plt.show()
    plt.savefig(file3+'/'+'p1/p1_ _'+item+'_.png')
    plt.close()
