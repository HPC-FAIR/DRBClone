import os 
import pandas as pd 


data_path = 'OMP-unseen-test'
files = os.listdir(data_path) 


k = 5 


for file in files: 
    
    
    print(file) 

    df = pd.read_csv(os.path.join(data_path, file), header=None) 
        
    # print(df)    

    df = df.sort_values(by=[2], ascending=False)
    # print(df) 

    print('top {}'.format(k)) 
    print(df[[0, 1, 2]][:k])
    print()


