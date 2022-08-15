import os 
import pandas as pd 
from os import walk

rootdir= 'OMP-unseen-test'
unseen = [] 
for file in os.listdir(rootdir):
	d = os.path.join(rootdir, file)
	if os.path.isdir(d):
		for fl in os.listdir(d):
			unseen.append(os.path.join(d, fl))


print(unseen)

files = os.listdir('.') 
files = [f for f in files if f.split('.')[-1]=='csv']

print(files)
no = ['cosine_similarity_distanceBase_2D.csv', 'cosine_similarity_distanceBase-old.csv']

for file in files: 
	if file in no: 
		files.remove(file) 
	
unseen += files
# files = os.listdir('.')
# files = os.list


# # just fill the name with the ones that needs to get sorted 
# name = 'consin_similarity_codeBERT.csv'

for name in unseen: 
	print(name)
	df = pd.read_csv(name, header=None)
	# print(df)
	df[3] = df[1].apply(lambda x: x.rsplit('.',2)[0])
	df['part'] = df[1].apply(lambda x: int(x.split('.')[-2])).astype(int)

	df = df.sort_values(by=[0, 3, 'part'])
	df.drop(columns=[3, 'part'], inplace=True)
	# print(df)

	df.to_csv(name, header=None, index=False)



# name = 'sourcerCC/similarityCC.csv'

# print(name)
# df = pd.read_csv(name, header=None)
# print(df)
# df[3] = df[1].apply(lambda x: x.rsplit('.',2)[0])
# df['part'] = df[1].apply(lambda x: int(x.split('.')[-2])).astype(int)

# df = df.sort_values(by=[0, 3, 'part'])
# df.drop(columns=[3, 'part'], inplace=True)
# print(df)


# df.to_csv(name, header=None, index=False)
