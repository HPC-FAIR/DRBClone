import os 
import numpy as np 
import pandas as pd 


def read_stats(path): 

	maps = dict() 
	with open(path, 'r')as f: 
		for line in f.readlines(): 
			data = line.split(',')
			id = data[1]
			name = data[3].split('/')[-1].strip('\"')
			maps[id] = name

	return maps 

def mapping(maps, file): 

	existed = dict()
	
	with open(file, 'r') as f: 
		for line in f.readlines():
			data = line.split(',')
			row = [maps[data[1]], maps[data[3]], float(data[4]) ]
			reverse_row = [maps[data[3]],  maps[data[1]], float(data[4]) ]

			existed[(maps[data[1]], maps[data[3]])] = float(data[4])
			existed[(maps[data[3]], maps[data[1]])] = float(data[4])
			# print(maps[id1], maps[id2], value)
			# df.loc[len(df.index)] = row 
			# df.loc[len(df.index)] = reverse_row 
			# df = pd.concat([df, row], ignore_index = True)
			# df = pd.concat([df, reverse_row], ignore_index = True)
			# existed.append((maps[data[1]], maps[data[3]]))
			# existed.append((maps[data[3]], maps[data[1]]))

	names = list(maps.values())
	
	comb_array = np.array(np.meshgrid(names, names)).T.reshape(-1, 2)
	df = pd.DataFrame()
	df[0] = comb_array[:,0]
	df[1] = comb_array[:,1]

	value = []
	print(len(comb_array))
	for pair in comb_array: 
		id1, id2 = pair[0], pair[1]
		print(id1, id2) 

		if id1 == id2: 
			value.append(1.0)
		elif (id1, id2) in existed.keys(): 
			value.append(existed[(id1, id2)])
		else: 
			value.append(0.1)

		# if id1 == id2: 
		# 	one = [id1, id2, 1.0]
		# 	df.loc[len(df.index)] = one 
		# 	# df = pd.concat([df, one], ignore_index=True)

		# elif df[(df['name1'] == id1) & (df['name2'] == id2)] is not None: 
		# 	pass
		# elif df[(df['name1'] == id2) & (df['name2'] == id1)] is not None: 
		# 	pass
		# else: 
		# 	rest = [id1, id2, 0.1]
		# 	df.loc[len(df.index)] = rest 
			# df = pd.concat([df, rest], ignore_index=True)

	print(len(value))
	df[2] = value
	df = df.sort_values(by=[0, 1])
	
	return df 
			
maps = read_stats('files-stats-0.stats')
print(maps)



# print(names) 


# print(comb_array)



# df = df.sort_values(by=[0,1])
# print(df)

df = mapping(maps, 'results.pairs')

print(df) 

df.to_csv('similarityCC.csv')