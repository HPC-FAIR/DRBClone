import os 

import pandas as pd 


data_path = "cosine_final"


k = 5 


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

        # drop in the same DRB file, which is likely havin same loop structures 
        df['same_file'] = df.apply(lambda row: str(row[0])[:5] == str(row[1])[:5], axis=1)
        df =  df.drop(df[df['same_file'] == True].index)

        # drop var/orig pairs.  note DRB077 and DRB125 share same substring in name (should not be removed).  
        df['orig_var'] = df.apply(lambda row:  str(row[0])[6:].split(".c")[0] != str(row[1])[6:].split(".c")[0] and (str(row[0])[6:].split(".c")[0].replace("orig","var") == str(row[1])[6:].split(".c")[0] or str(row[0])[6:].split(".c")[0].replace("var","orig") == str(row[1])[6:].split(".c")[0]), axis=1)
#        print(df[df['orig_var'] == True])
        df =  df.drop(df[df['orig_var'] == True].index)

        # drop indirectaccess, due to highly similar
        df['indirectaccess'] = df.apply(lambda row: str(row[0]).find("indirectaccess") != -1 and  str(row[1]).find("indirectacces") != -1, axis=1)
        df =  df.drop(df[df['indirectaccess'] == True].index)

        # drop 1.0 score
        df['perfectscore'] = df.apply(lambda row: row[2] == 1.0 , axis=1)
        df =  df.drop(df[df['perfectscore'] == True].index)

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




