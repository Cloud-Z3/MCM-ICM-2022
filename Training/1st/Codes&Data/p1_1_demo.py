# This is a demo, or, let's say, a lib.
# It's only for match1, considering 15 min timespan.

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import networkx as nx
import matplotlib
matplotlib.rcParams['font.sans-serif']=['Times New Roman']

file1='2020_Problem_D_DATA'
file2='2020_Problem_D_DATA_After_Pro'
file3='Image'
file='passingevents_match1.csv'
p1='Problem1'
p2='Problem2'
p3='Problem3'
p4='Problem4'

def simplemap(coordinate):
    x1=0
    y1=-50
    span=10
    x=coordinate[0]
    y=coordinate[1]
    return [x1+x*2,y1+y*1]

#matches=pd.read_csv(file1+'/matches.csv')
#passingevents=pd.read_csv(file1+'/passingevents.csv')
#fullevents=pd.read_csv(file1+'/fullevents.csv')

def nodeedgeget(span,file):
    passingevents_match1=pd.read_csv(file2+'/'+p1+file)
    num=len(passingevents_match1)

    nodes=[]
    for i in passingevents_match1.index:
        if passingevents_match1['EventTime'][i]<span[0]:
            continue
        if passingevents_match1['EventTime'][i]>span[1]:
            break
        if passingevents_match1['TeamID'][i]=='Huskies':
            nodes.append(passingevents_match1['OriginPlayerID'][i])
            nodes.append(passingevents_match1['DestinationPlayerID'][i])
    nodes=list(set(nodes))#节点

    nodeid=dict()
    for i in range(len(nodes)):
        nodeid[nodes[i]]=i

    coordinate=dict()
    for i in passingevents_match1.index:
        node1 = passingevents_match1['OriginPlayerID'][i]
        node2 = passingevents_match1['DestinationPlayerID'][i]
        if passingevents_match1['TeamID'][i]!='Huskies':
            continue
        if passingevents_match1['EventTime'][i]<span[0]:
            continue
        if passingevents_match1['EventTime'][i]>span[1]:
            break
        if node1 not in coordinate:
            coordinate[node1]=[[passingevents_match1['EventOrigin_x'][i]],[passingevents_match1['EventOrigin_y'][i]]]
        else:
            coordinate[node1][0].append(passingevents_match1['EventOrigin_x'][i])
            coordinate[node1][1].append(passingevents_match1['EventOrigin_y'][i])
        if node2 not in coordinate:
            coordinate[node2]=[[passingevents_match1['EventDestination_x'][i]],[passingevents_match1['EventDestination_y'][i]]]
        else:
            coordinate[node2][0].append(passingevents_match1['EventDestination_x'][i])
            coordinate[node2][1].append(passingevents_match1['EventDestination_y'][i])

    for node in nodes:
        a = sum(coordinate[node][0])/len(coordinate[node][0])
        b = sum(coordinate[node][1])/len(coordinate[node][1])
        coordinate[node][0]=a
        coordinate[node][1]=b

    adjmatrix=[[0 for _ in range(len(nodes))] for _ in range(len(nodes))]
    for i in range(num):
        if passingevents_match1['TeamID'][i] != 'Huskies':
            continue
        if passingevents_match1['EventTime'][i]<span[0]:
            continue
        if passingevents_match1['EventTime'][i]>span[1]:
            break
        a=passingevents_match1['OriginPlayerID'][i]
        b=passingevents_match1['DestinationPlayerID'][i]
        adjmatrix[nodeid[a]][nodeid[b]]+=1

    G = nx.Graph()#无向图
    for node in nodes:
        G.add_node(node)
    for i in range(len(adjmatrix)):
        for j in range(len(adjmatrix)):
            if adjmatrix[i][j]!=0:
                G.add_edge(nodes[i],nodes[j],weight=adjmatrix[i][j])

    pos=nx.spring_layout(G)
    nx.draw(G,pos)
    node_label={}
    for node in G.nodes:
        node_label[node]=node
    edge_label=nx.get_edge_attributes(G,'weight')
    nx.draw_networkx_labels(G,pos,labels=node_label)
    nx.draw_networkx_edge_labels(G,pos,edge_labels=edge_label)
    plt.savefig(file3+'/p1_fig1.png',dpi=1000)
    #plt.show()

    #Gephi所需信息
    df_nodes=[]
    for i,node in enumerate(nodes):
        coor=simplemap(coordinate[node])
        df_nodes.append(['n'+str(i),node.split('_')[1],coor[0],coor[1],node.split('_')[1][0]])
    #print(df_nodes)

    df_edges=[]
    index=0
    for i in range(len(nodes)):
        for j in range(len(nodes)):
            if adjmatrix[i][j]!=0:
                df_edges.append(['n'+str(i),'n'+str(j),'Directed',index,adjmatrix[i][j]])
                index+=1

    df_nodes=pd.DataFrame(df_nodes,columns=['Id','Label','longitude','latitude','color'])
    #df_nodes.to_csv(file2+'/'+p1+'/'+'dataforp1_1_node.csv',index=False)
    df_edges=pd.DataFrame(df_edges,columns=['Source','Target','Type','Id','Weight'])
    #df_edges.to_csv(file2+'/'+p1+'/'+'dataforp1_1_edge.csv',index=False)
    return df_nodes,df_edges

df_nodes,df_edges=nodeedgeget([0,900],'/passingevents_match1.csv')
#df_nodes.to_csv(file2+'/'+p1+'/'+'dataforp1_1_node.csv',index=False)
#df_edges.to_csv(file2+'/'+p1+'/'+'dataforp1_1_edge.csv',index=False)