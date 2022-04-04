import networkx as nx                            #导入NetworkX包，为了少打几个字母，将其重命名为nx
import pandas as pd
nodefile = f'./data/1_nodes.csv'
edgefile = f'./data/0_network_draw.csv'

nodefile=pd.read_csv(nodefile)
print(nodefile)
edgefile=pd.read_csv(edgefile)
print(edgefile)

G = nx.DiGraph()
for i in range(len(nodefile)):
    G.add_node(i)
for i in range(len(edgefile)):
    G.add_edge(edgefile['Source'][i],edgefile['Target'][i])

# G = nx.DiGraph()                                        #建立一个空的无向图G
# G.add_node(1)                                        #添加一个节点1
# G.add_edge(2,3)                                     #添加一条边2-3（隐含着添加了两个节点2、3）
# G.add_edge(3,2)                                     #对于无向图，边3-2与边2-3被认为是一条边
# print(G.nodes())                                       #输出全部的节点
# print(G.edges())                                       #输出全部的边
# print(G.number_of_edges())                    #输出边的数量
# path1=nx.has_path(G,source=1,target=2)
# path=nx.shortest_path_length(G,source=0,target=3)
n=len(nodefile)
index1=0
path_length=0
print(000)
print(nx.average_clustering(G))
print(111)
print(nx.average_shortest_path_length(G))
# for i in range(n):
#     for j in range(n):
#         if nx.has_path(G,source=i,target=j):
#             print(index1)
#             path_length+=nx.shortest_path_length(G,source=i,target=j)
#             index1+=1
# print(path_length)
# print(index1)
# print(path)
# print(path1)