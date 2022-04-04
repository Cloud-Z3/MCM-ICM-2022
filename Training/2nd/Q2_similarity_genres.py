from Q2_lib import *

import pandas as pd

def distance_wh_genres(agenre):
    musician=genre_musician[agenre]
    n=len(musician)
    print('n',n)
    alldist=0
    for i in range(n):
        print(i)
        m1=musician[i]
        for j in range(i+1,n):
            m2=musician[j]
            # s=m1+','+m2
            # if s not in dist:
            #     dist[s]=distance_musician(m1,m2)
            alldist+=distance_musician(m1,m2)
    return alldist*2/n/(n-1) if n!=1 else 0

def distance_bt_genres(genre1,genre2):
    musician1,musician2=genre_musician[genre1],genre_musician[genre2]
    n1,n2=map(len,[musician1,musician2])
    alldist=0
    print(n1,n2)
    for i in range(n1):
        print(i)
        m1=musician1[i]
        for j in range(n2):
            #print('j',j)
            # m2=musician2[j]
            # s = m1 + ',' + m2
            # if s not in dist:
            #     dist[s] = distance_musician(m1, m2)
            alldist+=distance_musician(m1, m2)
    return alldist/n1/n2

df_inf = pd.read_csv('./Data/influence_data.csv')
influencer=df_inf['influencer_name']
follower=df_inf['follower_name']
genre = dict()
for i in df_inf.index:
    m1=influencer[i]
    m2=follower[i]
    if m1 not in genre:
        genre[m1]=df_inf['influencer_main_genre'][i]
    if m2 not in genre:
        genre[m2]=df_inf['follower_main_genre'][i]
genres=list(set(genre.values()))
genre_musician=dict()
for item in genre:
    if genre[item] not in genre_musician:
        genre_musician[genre[item]]=[item]
    else:
        genre_musician[genre[item]].append(item)

dist=dict()
gen_can=['Folk','Blues','Vocal','New Age','International','Electronic']
n=len(gen_can)
matrix1=[[0 for _ in range(n)] for _ in range(n)]
matrix2=[[0 for _ in range(n)] for _ in range(n)]
for i in range(n):
    print('i',i)
    genre1=gen_can[i]
    for j in range(i,n):
        print('j',j)
        genre2=gen_can[j]
        if i==j:
            wh=distance_wh_genres(genre1)
            matrix1[i][i] = wh
            matrix2[i][i] = 1 / (1 + wh)
        else:
            bt=distance_bt_genres(genre1,genre2)
            matrix1[i][j] = bt
            matrix1[j][i] = bt
            matrix2[i][j] = 1/(1+bt)
            matrix2[j][i] = 1/(1+bt)
df_out=pd.DataFrame(data=matrix1,index=gen_can,columns=gen_can)
df_out.to_csv('./Data/p2/distance_genres.csv')
df_out=pd.DataFrame(data=matrix2,index=gen_can,columns=gen_can)
df_out.to_csv('./Data/p2/similarity_genres.csv')

# ,'Blues','Vocal','New Age','International','Electronic'