import os 

import pandas as pd 


data_path = "cosine_final"


k = 3 


files = os.listdir(data_path) 
print(files)
dfs = []
for file in files: 
    
        df = pd.read_csv(os.path.join(data_path, file), header=None) 

        # print(df) 

        df = df[df[0] != df[1]] 


        # print("run")  
        
        df['check_string'] = df.apply(lambda row: ''.join(sorted([row[0], row[1]])), axis=1)
        df =  df.drop_duplicates('check_string')

    

        df = df.sort_values(by=[2], ascending=False) 

        
        dfs.append(df[[0, 1, 2]][:k]) 


print(dfs) 
df = pd.DataFrame()
for file in files: 
    
        
    temp_df = pd.read_csv(os.path.join(data_path, file), header=None) 
    temp_df['model'] = file.split('_')[-1].split('.')[0]

    df = pd.concat([df, temp_df])


for f, d in zip(files, dfs): 
    print(f) 
    
    
    for pair in zip(d[0], d[1]): 
        
        output = df[(df[0] == pair[0]) & (df[1] == pair[1])]
        print(output)

    print() 
    print()




