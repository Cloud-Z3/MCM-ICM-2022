import pandas as pd
import numpy as np
from collections import Counter
import os
from Q1_lib import *


df_influence=pd.read_csv('./data/influence_data.csv')
df_artist=pd.read_csv('./data/data_by_artist.csv')
df_year=pd.read_csv('./data/data_by_year.csv')
df_music=pd.read_csv('./data/full_music_data.csv')

df_music['duration_ms']=df_music['duration_ms'].astype(float)
df_music['popularity']=df_music['popularity'].astype(float)
df_music['year']=df_music['year'].astype(float)
df_artist['count']=df_artist['count'].astype(float)


for column in df_music.columns:
    if column in ['release_date','song_title (censored)','artist_names','artists_id','key','explicit']:
        continue
    minv=min(df_music[column])
    maxv=max(df_music[column])
    for i in df_music.index:
        # print(df_music[column][i],(df_music[column][i]-minv)/(maxv-minv))
        df_music[column][i]=(df_music[column][i]-minv)/(maxv-minv)
# print(abc)
df_music.to_csv('./data/full_music_data_ap.csv')


for column in df_artist.columns:
    if column in ['release_date','song_title (censored)','artist_name','artist_id','key','explicit']:
        continue
    minv=min(df_artist[column])
    maxv=max(df_artist[column])
    for i in df_artist.index:
        df_artist[column][i]=(df_artist[column][i]-minv)/(maxv-minv)
df_artist.to_csv('./data/data_by_artist_ap.csv')

for column in df_year.columns:
    if column in ['year','song_title (censored)','artist_name','artist_id','key','explicit']:
        continue
    minv=min(df_year[column])
    maxv=max(df_year[column])
    for i in df_year.index:
        df_year[column][i]=(df_year[column][i]-minv)/(maxv-minv)
df_year.to_csv('./data/data_by_year_ap.csv')
