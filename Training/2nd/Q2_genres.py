import pandas as pd
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
genre_musician=dict()
for item in genre:
    if genre[item] not in genre_musician:
        genre_musician[genre[item]]=[item]
    else:
        genre_musician[genre[item]].append(item)
g_num=[[len(genre_musician[item]),item] for item in genre_musician]
g_num.sort()
print(g_num)