import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

file1='2020_Problem_D_DATA'
file2='2020_Problem_D_DATA_After_Pro'
file3='Image'
p1='Problem1'
p2='Problem2'
p3='Problem3'
p4='Problem4'

def matchget(matchid):
    matches=pd.read_csv(file1+'/matches.csv')
    passingevents=pd.read_csv(file1+'/passingevents.csv')
    #fullevents=pd.read_csv(file1+'/fullevents.csv')

    matrix=[]
    for i in passingevents.index:
        if passingevents['MatchID'][i]==matchid:
            matrix.append([passingevents[c][i] for c in passingevents.columns])

    df=pd.DataFrame(matrix,columns=passingevents.columns)
    for i in df.index:
        if df['MatchPeriod'][i]=='2H':
            df['EventTime'][i]+=3600
    df.to_csv(file2+'/'+p1+'/passingevents_match'+str(matchid)+'.csv',index=False)

matchget(1)