from math import log,e
import pandas as pd

df_music_ap=pd.read_csv('./data/full_music_data_ap.csv')
df_artist_ap=pd.read_csv('./data/data_by_artist_ap.csv')
df_year_ap=pd.read_csv('./data/data_by_year_ap.csv')
df=pd.read_csv("./data/influence_data.csv")
influencer=df['influencer_name']
follower=df['follower_name']

musician=set(df['influencer_name'])|set(df['follower_name'])
musician=list(musician)
#print(musician)
mu_id=dict()
for i,m in enumerate(musician):
    mu_id[m]=i

music_id=dict()
for i in df_music_ap.index:
    music_id[df_music_ap['song_title (censored)'][i]]=i

def plnp(p):
    return p*log(p) if p!=0 else 0

def E(colum):
    minv=min(colum)
    maxv=max(colum)
    n=len(colum)
    coloum=[(c-minv)/(maxv-minv) for c in colum]
    s=sum(coloum)
    coloum = [c/s for c in coloum]
    return -sum([plnp(c) for c in coloum])/log(n)

def weight(Elist):
    k=len(Elist)
    det=k-sum(Elist)
    return [(1-E)/det for E in Elist]

def WeightCal(df,colums):
    Elist=[]
    n=len(colums)
    for colum in colums:
        Elist.append(E(df[colum]))
    w=weight(Elist)
    return [[colums[i],w[i]] for i in range(n)]

def distance(df1:pd.DataFrame,df2:pd.DataFrame,weight)->float:
    id1=df1.index[0]
    id2=df2.index[0]
    columns,weight=zip(*weight)
    # print(columns)
    # print(weight)
    return (sum([weight[i]*(df1[column][id1]-df2[column][id2])**2 for i,column in enumerate(columns)]))**0.5

def distance_attribute(a,b):
    aid,bid=music_id[a],music_id[b]
    return distance(df_music_ap.loc[[aid]],df_music_ap.loc[[bid]],weight_music)

def distance_musician(a,b):
    aid,bid=mu_id[a],mu_id[b]
    return distance(df_artist_ap.loc[[aid]],df_artist_ap.loc[[bid]],weight_musician)

def hasdoff(A,B):
    lena,lenb=len(A),len(B)
    dist_matrix=[[distance_musician(A[i],B[j]) for j in range(lenb)] for i in range(lena)]
    max1=max([min(line) for line in dist_matrix])
    max2=max([min([dist_matrix[i][j] for i in range(lena)]) for j in range(lenb)])
    return max(max1,max2)

def distance_music(a,b):
    aid,bid=music_id[a],music_id[b]
    A,B=map(eval,[df_music_ap['artist_names'][aid],df_music_ap['artist_names'][bid]])
    return distance_attribute(a,b)+hasdoff(A,B)

def similarity(a,b):
    return 1/(1+distance_music(a,b))

df_music=pd.read_csv('./data/full_music_data.csv')
df_artist=pd.read_csv('./data/data_by_artist.csv')

colums1=['danceability','energy','valence','tempo','loudness','mode','acousticness','instrumentalness','liveness','speechiness','duration_ms','popularity','year']
weight_music=WeightCal(df_music,colums1)
weight_music_dict=dict()
for w in weight_music:
    weight_music_dict[w[0]]=w[1]
colums2=['danceability','energy','valence','tempo','loudness','mode','acousticness','instrumentalness','liveness','speechiness','duration_ms','popularity','count']
weight_musician=WeightCal(df_artist,colums2)
weight_musician_dict=dict()
for w in weight_musician:
    weight_musician_dict[w[0]]=w[1]


