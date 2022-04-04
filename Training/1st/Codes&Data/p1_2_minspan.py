from p1_1_demo import *

file='/passingevents_match1.csv'
for i in range(8):
    span=[i*900,(i+1)*900]
    df_nodes,df_edges=nodeedgeget(span=span,file=file)
    print(i)
    #df_nodes.to_csv(file2 + '/' + p1 + '/' + 'dataforp1_'+str(i+1)+'_node.csv', index=False)
    #df_edges.to_csv(file2 + '/' + p1 + '/' + 'dataforp1_'+str(i+1)+'_edge.csv', index=False)
