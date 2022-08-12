import os
import numpy as np 
import random
import json
import re
from tqdm import tqdm

def files(path):
    g = os.walk(path) 
    file=[]
    for path,dir_list,file_list in g:  
        for file_name in file_list:  
            file.append(os.path.join(path, file_name))
    return file

def remove_comments(func): 
    pattern = r'(\".*?\"|\'.*?\')|(/\*.*?\*/|//[^\r\n]*$)'  
    regex = re.compile(pattern, re.MULTILINE | re.DOTALL) 
    
    def _replacer(match): 
        # print(match)
        if match.group(2) is not None: 
            return ""
        else: 
            return match.group(1) 

    return regex.sub(_replacer, func)

def read_stats(path): 

	maps = dict() 
	with open(path, 'r')as f: 
		for line in f.readlines(): 
			data = line.split(',')
			id = data[1]
			name = data[3].strip('\"')
			maps[id] = name

	return maps 


def create_data(maps):
	

	with open("data.jsonl",'w') as f:

		for m in tqdm(maps,total=len(maps.keys())):
			js = {}
			js['idx'] = m
			js['func']=remove_comments(open(maps[m],encoding='latin-1').read())
			f.write(json.dumps(js)+'\n')


def clean_pair(pairs, maps): 
	with open("labels.txt", 'w') as f: 

		ps = []
		with open(pairs, 'r') as fl: 
			for line in fl.readlines():
				data = line.split(',')
				pair = data[1] + '\t' + data[3].strip('\n') + '\t' + '1' + '\n'
				# print(pair)
				f.write(pair) 
				ps.append((data[1], data[3].strip('\n')))

	
		rand = np.random.permutation(list(maps.keys()))
		temp = [(i, j) for i, j in zip(list(maps.keys()), rand)]
		for t in temp: 
			if t in ps:
				print(t) 
				continue
			else: 
				f.write(t[0] + '\t' + t[1] + '\t' + '0' + '\n')
	

def main(): 
	file = "files-stats-0.stats"
	pairs = "results-POJ.pairs"

	# create_data()

	# maps = read_stats(file)
	# print(maps)
	# create_data(maps)
	# clean_pair(pairs, maps)


	with open('labels.txt', 'r') as f: 
		store =[]
		for line in f.readlines(): 
			store.append(tuple(line.split('\t')))
		
		# print(store)
		random.shuffle(store) 
		print(len(store))
		train_len = int(len(store) * .7)
		valid_len = int(len(store) * .1) 
		test_len = len(store) - valid_len - train_len
		

		print('train', train_len) 
		print('valid', valid_len) 
		print('test', test_len)
		with open('train.txt', 'w') as train: 

			for s in store[:train_len]: 
				train.write(s[0] + '\t' + s[1] + '\t' + s[2])

		with open('valid.txt', 'w') as valid: 
			for s in store[train_len:train_len+valid_len]: 
				valid.write(s[0] + '\t' + s[1] + '\t' + s[2])


		with open('test.txt', 'w') as test: 
			for s in store[train_len+valid_len:len(store)]: 
				test.write(s[0] + '\t' + s[1] + '\t' + s[2]) 
		
		# print(store)

if __name__ == '__main__': 
	main() 

