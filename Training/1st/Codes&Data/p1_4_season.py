from p1_1_demo import *


span=[0,7200]
df_nodes,df_edges=nodeedgeget(span=span,file='/passingevents.csv')
df_nodes.to_csv(file2 + '/' + p1 + '/' + 'dataforp1_17_node.csv', index=False)
df_edges.to_csv(file2 + '/' + p1 + '/' + 'dataforp1_17_edge.csv', index=False)
