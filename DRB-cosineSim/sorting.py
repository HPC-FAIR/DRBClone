import os 
import pandas as pd 


# just fill the name with the ones that needs to get sorted 

name = 'consin_similarity_codeBERT.csv'


df = pd.read_csv(name, header=None)
# print(df)
df[3] = df[1].apply(lambda x: x.rsplit('.',2)[0])
df['part'] = df[1].apply(lambda x: int(x.split('.')[-2])).astype(int)

df = df.sort_values(by=[0, 3, 'part'])
df.drop(columns=[3, 'part'], inplace=True)
# print(df)

df.to_csv(name, header=None, index=False)
