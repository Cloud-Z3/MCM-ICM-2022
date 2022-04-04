# Find the Team PlayeRank.

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import networkx as nx
import matplotlib
import warnings
import copy
import math
warnings.filterwarnings('ignore')
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

columns=['Flow Centrality','Team PlayeRank','MaxEigenvalue','Connectivity','Clustering Coefficient',\
         'Shortest-path Length']

matches=pd.read_csv(file1+'/'+'matches.csv')
print(matches)
for i,c in enumerate(columns):
    if i==0 or i==1:
        df = pd.read_csv(file2 + '/' + p2 + '/' + c + '.csv')
    else:
        df = pd.read_csv(file2 + '/' + p1 + '/' + c + '.csv')
    matches[c]=df[c]
matches.to_csv(file2 + '/' + p2+'/MatchData.csv')
