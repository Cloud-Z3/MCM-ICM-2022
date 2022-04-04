# -*- coding: utf-8 -*-
"""
Created on Mon Aug 19 13:14:12 2019

@author: Administrator
"""

# -*- coding: utf-8 -*-
"""
Created on Sun Jun 16 20:13:42 2019

@author: Administrator
"""

"""

这个函数的作用是将一个矩阵给转换成一个图，
矩阵以多维列表的形式存在，即列表的列表
此处的转换是针对无向图

根据邻接矩阵得到图之后，我们就可以调用networkx
里面的各种函数来分析图的性质，比如度分布，
平均路径程度，聚类系数等一系列图的拓扑性质

"""
import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt

def matrix_to_graph(matrix):

    G = nx.DiGraph()
    n=len(matrix)
    nodes=list(range(n))
    for i in range(n):
        for j in range(n):
            if (matrix[i][j] != 0):
                G.add_edge(i, j)

    position = nx.circular_layout(G)
    nx.draw_networkx_nodes(G, position, nodelist=nodes, node_color="r")
    nx.draw_networkx_edges(G, position)
    #nx.draw_networkx_labels(G, position)
    plt.show()

    # print(nx.to_numpy_matrix(G))
    # print(G.degree()) #节点的度
    # print(nx.clustering(G))#节点的聚类系数

    print(nx.average_clustering(G))  # 整个图的聚集系数
    print("---------------------------------------")
    print(nx.average_shortest_path_length(G))  # 图的平均路径长度


# print(nx.number_connected_components(G))#图的连通分支
# print(nx.to_numpy_matrix(G))

df_node=pd.read_csv(f'./Data/p1/1_nodes.csv')
df_edge=pd.read_csv(f'./Data/p1/0_network_draw.csv')
n=len(df_node)
adj = [[0 for _ in range(n)] for _ in range(n)]
for i in df_edge.index:
    a = df_edge['Source'][i]
    b = df_edge['Target'][i]
    adj[a][b] += 1

matrix_to_graph(adj)
