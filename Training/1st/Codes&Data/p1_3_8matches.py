from p1_1_demo import *
from p1_0_preProcess import matchget

for i in range(8):
    print(i)
    matchget(i+1)
    span=[0,7200]
    df_nodes,df_edges=nodeedgeget(span=span,file='/passingevents_match'+str(i+1)+'.csv')
    df_nodes.to_csv(file2 + '/' + p1 + '/' + 'dataforp1_'+str(i+8+1)+'_node.csv', index=False)
    df_edges.to_csv(file2 + '/' + p1 + '/' + 'dataforp1_'+str(i+8+1)+'_edge.csv', index=False)
