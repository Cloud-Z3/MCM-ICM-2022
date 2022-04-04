import collections
import numpy as np
import networkx as nx
from sklearn.cluster import DBSCAN
import pandas as pd
from Q1_lib import *

class WalkSCAN:

    def __init__(self, nb_steps=2, eps=0.1, min_samples=3):
        self.nb_steps = nb_steps
        self.eps = eps
        self.min_samples = min_samples
        self.dbscan_ = DBSCAN(eps=self.eps, min_samples=self.min_samples)

    def load(self, graph, init_vector):
        self.graph = graph.copy()
        self.init_vector = init_vector.copy()

    def embed_nodes(self):
        p = {0: self.init_vector.copy()}
        for t in range(self.nb_steps):
            p[t + 1] = collections.defaultdict(int)
            for v in p[t]:
                for (_, w, e_data) in self.graph.edges(v, data=True):
                    if 'weight' in e_data:
                        self.weighted_ = True
                        p[t + 1][w] += float(e_data['weight']) / float(self.graph.degree(v, weight='weight')) * p[t][v]
                    else:
                        self.weighted_ = False
                        p[t + 1][w] += 1.0 / float(self.graph.degree(v)) * p[t][v]
        self.embedded_value_ = dict()
        self.embedded_nodes_ = list()
        for v in p[self.nb_steps]:
            self.embedded_nodes_.append(v)
            self.embedded_value_[v] = np.array([p[t + 1][v] for t in range(self.nb_steps)])
        self.nb_embedded_nodes_ = len(self.embedded_nodes_)

    def find_cores(self):
        if self.nb_embedded_nodes_ > 0:
            P = np.zeros((self.nb_embedded_nodes_, self.nb_steps))
            for (i, node) in enumerate(self.embedded_nodes_):
                P[i, :] = self.embedded_value_[node]
            self.dbscan_.fit(P)
            self.cores_ = collections.defaultdict(set)
            self.outliers_ = set()
            for (i, node) in enumerate(self.embedded_nodes_):
                label = self.dbscan_.labels_[i]
                if label >= 0:
                    self.cores_[label].add(node)
                else:
                    self.outliers_.add(node)
        else:
            self.cores_ = {}
            self.outliers_ = set()

    def compute_core_average_value(self):
        self.core_average_value_ = dict()
        for (core_id, core) in list(self.cores_.items()):
            self.core_average_value_[core_id] = np.zeros(self.nb_steps)
            for node in core:
                for t in range(self.nb_steps):
                    self.core_average_value_[core_id][t] += self.embedded_value_[node][t] / float(len(core))

    def sort_cores(self):
        self.sorted_core_ids_ = list(self.cores_.keys())
        self.sorted_core_ids_.sort(key=lambda i: list(self.core_average_value_[i]),
                                   reverse=True)
        self.sorted_cores_ = [self.cores_[i] for i in self.sorted_core_ids_]

    def aggregate_outliers(self):
        self.communities_ = list()
        for core in self.sorted_cores_:
            community = core.copy()
            for node in core:
                community |= set(nx.neighbors(self.graph, node)) & self.outliers_
            self.communities_.append(community)

    def detect_communities(self, graph, init_vector):
        self.load(graph, init_vector)
        self.embed_nodes()
        self.find_cores()
        self.compute_core_average_value()
        self.sort_cores()
        self.aggregate_outliers()

df=pd.read_csv("./data/influence_data.csv")
influencer=df['influencer_name']
follower=df['follower_name']

musician=[]
for i in df.index:
    if influencer[i] not in musician:
        musician.append(influencer[i])
    if follower[i] not in musician:
        musician.append(follower[i])
n=len(musician)
mu_id=dict()
for i,m in enumerate(musician):
    mu_id[m]=i

G = nx.DiGraph()
for i in range(n):
    G.add_node(i)
for i in df.index:
    a=mu_id[influencer[i]]
    b=mu_id[follower[i]]
    G.add_edge(a,b)

#print(G.nodes, G.edges, G.number_of_nodes(), G.number_of_edges())
# Create a random graph with two partitions
#G = nx.random_partition_graph([10, 15], 0.9, 0.01)
#print(G)

# Create a WalkSCAN instance
ws = WalkSCAN(nb_steps=15, eps=0.000005, min_samples=2)

# Initialization vector for the random walk
init_vector = {0: 0.1, 10: 0.1, 100:0.1, 1000:0.1, 5000:0.1, 5200:0.1, 5300:0.1, 5400:0.1, 5500:0.1, 5560:0.1}

# Compute the communities
ws.detect_communities(G, init_vector)

# Print the best community
#print(ws.communities_)


color=dict()
c=[chr(ord('A')+i) for i in range(26)]+[chr(ord('a')+i) for i in range(26)]
for i,commmunity in enumerate(ws.communities_):
    for item in commmunity:
        if item not in color:
            color[item]=c[i]
for i in range(len(G.nodes)):
    if i not in color:
        color[i]=c[len(ws.communities_)]

adj=[[0 for _ in range(n)] for _ in range(n)]

for i in df.index:
    if influencer[i] in musician and follower[i] in musician:
        a,b=mu_id[influencer[i]],mu_id[follower[i]]
        adj[a][b]+=1
#print(adj)

matrix_=[]
Id=0
for i in range(n):
    for j in range(n):
        if adj[i][j]!=0:
            matrix_.append([i,j,'Directed',Id,adj[i][j],color[i]])
            Id+=1

df_out=pd.DataFrame(data=matrix_,columns=['Source','Target','Type','Id','Weight','color'])
df_out.to_csv('./Data/p1/4_network_draw.csv')
# 边

matrix_=[]
for i in range(n):
    weight=sum(adj[i])
    matrix_.append([i,musician[i],weight,color[i],c.index(color[i])])
df_out=pd.DataFrame(data=matrix_,columns=['Id','Label','Weight','color','modularity_class'])
# 节点
df_out.to_csv('./Data/p1/5_nodes.csv',index=False)
df_out.to_csv('./Data/p1/6_community_mwbased.csv',index=False)

print(len(ws.communities_))

itera=0
for community in ws.communities_:
    n=len(community)
    if not 10<=len(community)<=40:
        continue
    df.loc[community].to_csv(f"./Data/p1/subnet_data/subnet{str(itera)}.csv", index=False)
    file1=f'./Data/p1/subnet_edge&data/nodes_{str(itera)}.csv'
    file2=f'./Data/p1/subnet_edge&data/edges_{str(itera)}.csv'
    musicians=[musician[i] for i in community]
    line=[]
    for i in df.index:
        if influencer[i] in musicians and follower[i] in musicians:
            line.append(i)
    process2(df.loc[line],file1,file2)
    itera+=1
