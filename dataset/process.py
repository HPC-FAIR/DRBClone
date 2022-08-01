import os 
import json
import re 
import numpy as np 

with open('./parsed_data.json', 'r') as f: 

    js = json.load(f) 
    
    data = js['data']
    

    for d in data: 
        d['idx'] = d['file'].split('/')[-1].split('-')[0]
        del d['file']
        
        d['func'] = "" 
            


        print(d)



