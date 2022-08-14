import os 
import pandas as pd 


data_path = '../DRB-cosineSim/OMP-unseen-test/NPB-IS-1'
files = os.listdir(data_path) 


k = 5 


for file in files: 
    
    
    print(file) 

    df = pd.read_csv(os.path.join(data_path, file), header=None) 
        
    # print(df)    

    df = df.sort_values(by=[2], ascending=False)
    # print(df) 
    
    df = df[df[1]=='DRB004-antidep2-var-yes.c.1.txt'] 

    print('top {}'.format(k)) 
    print(df[[0, 1, 2]][:k])
    print()


