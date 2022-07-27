import torch 
import os 
import re 
from torch.utils.data import DataLoader, Dataset
from transformers import RobertaConfig, RobertaModel, RobertaTokenizer
from tqdm import tqdm, trange 
import numpy as np
import multiprocessing 
import random

cpu_cont = 16 

def readData(filepath, files, ids): 
    
    for f in files: 
        path = os.path.join(filepath, f)
        if os.path.isfile(path): 
            with open(path, 'r') as fl: 
                print(fl.read())


def get_token(item):
    id1, id2, data, tokenizer, block_size = item 

    code1 = ' '.join(data[id1].split())
    code2 = ' '.join(data[id2].split())  
    # print(id1, id2)

    # print(code1, code2)
    
    code1_token = tokenizer.tokenize(code1) 
    code2_token = tokenizer.tokenize(code2) 

    code1_tokens = code1_token[:block_size-2] 
    code1_tokens = [tokenizer.cls_token] + code1_tokens + [tokenizer.sep_token] 
    
    code2_tokens = code2_token[:block_size-2] 
    code2_tokens = [tokenizer.cls_token] + code2_tokens + [tokenizer.sep_token]
    
    code1_ids = tokenizer.convert_tokens_to_ids(code1_tokens) 
    padding_length = block_size - len(code1_ids) 
    code1_ids += [self.tokenizer.pad_token_id] * padding_length 
    
    code2_ids = tokenizer.convert_tokens_to_ids(code2_tokens) 
    padding_length = block_size - len(code2_ids) 
    code2_ids += [self.tokenizer.pad_token_id] * padding_length

    source_tokens = code1_tokens + code2_tokens 
    source_ids = code1_ids + code2_ids 
    print(source_ids)
    return source_ids


class DRB(Dataset): 
    



    def __init__(self, path, tokenizer, random_seed=0, type = 'train', block_size=500, pool=None): 
        self.path = path 

        self.data = [] 
        files = os.listdir(self.path) 
        data = dict() 

        for f in files:
            file_path = os.path.join(path, f)
            if os.path.isfile(file_path): 
                id = f.split('-',1)[0] 
                # print(id)
                with open(file_path, 'r') as fl: 
                    data[id] = fl.read()
        

        # random permutation to create a set of function 
        func1 = np.array(list(data.keys()))
        func2 = np.random.permutation(func1)
         
        dataset = []
        for id1, id2 in zip(func1, func2): 
            # print(id1, id2)
            dataset.append((id1, id2, data, tokenizer, block_size))
        
        # print(len(dataset))
        # print(dataset)
        if type == 'test': 
            # randomize 10% of the data 
            dataset = random.sample(dataset, int(len(dataset)*0.1))

        print(len(dataset)) 
        print(pool)
        print(pool.map(get_token, tqdm(dataset, total=len(dataset))))
        self.examples = pool.map(get_token, tqdm(dataset, total=len(dataset)))
    
        print(self.examples) 
    
    def __len__(self): 
    


        pass

    def __getitem__(self, idx):

        pass



def loadData(filepath): 
    files = os.listdir(filepath)
    print(len(files))
    id = { re.search('DRB(\d+)', f)[0]:f  for f in files if re.search('DRB(\d+)', f) is not None}
    #print(id)
    

    return id 

                

def main(): 
    cpu_cont = 88
    filepath = "./micro-benchmarks"
    pool = multiprocessing.Pool(cpu_cont)
    # id = loadData(filepath)
    
    # random permutation of matching two code
    # print(id.keys())
    # id1 = np.array(list(id.keys()))
    # id2 = id1 
    # id2 = np.random.permutation(id2)
    
    # print(id1) 
    # print(id2)
    # input_set = set()
    # for i in range(len(id1)): 
    #     input_set.add((id1[i], id2[i]))
    tokenizer = RobertaTokenizer.from_pretrained('microsoft/codebert-base') 
    
    
    
    
    
    
    
    
    dataset = DRB(filepath, tokenizer=tokenizer,  type='test', pool=pool) 

    # readData(filepath, files, id)





if __name__ == "__main__": 
    main()
