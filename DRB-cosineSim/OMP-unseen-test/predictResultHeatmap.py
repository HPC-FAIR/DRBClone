import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from matplotlib.patches import Rectangle


d1 ="NPB-IS-1"
d2 ="NPB-IS-2"
d3 ="rodinia-bfs-1"
d4 ="rodinia-hotspot_openmp-1"
d5 ="rodinia-lud_omp-1"
d6 ="rodinia-nn_openmp-1"

directory=[d1,d2,d3,d4,d5,d6]

prefix1="cosine_similarity"
prefix2="cosine_similarity_POJ"
prefix3="cosine_similarity_DRB"

prefix=[prefix1,prefix2,prefix3]
models=["M1","M2","M3"]

def convert(l):
    df2 = pd.DataFrame(index=range(1),columns=range(624),dtype=np.float64)
    df2 = df2.iloc[1:]
    idx = 0
    for i in range(0, 624):
        for n in range(0,1):
#            print(i,n,l[idx])
            df2.loc[n,i] = l[idx]
            idx = idx + 1
    return df2

fig, axs = plt.subplots(3,6,figsize=(18,8), gridspec_kw={'height_ratios': [1,1,1],'width_ratios':[1,1,1,1,1,1]})
for did, d in enumerate(directory,start=0):

    for pid, pre in enumerate(prefix, start=0):
        filename = d+"/"+pre+"_"+d+".csv"
#         print(filename)
        
        df = pd.read_csv(filename,float_precision='round_trip',header=None)
        df = df.iloc[:,2]
        df2 = convert(df)
#        print(df2)
        sns.heatmap( df2, cmap="rocket_r", ax=axs[pid][did],  vmin= 0., vmax=1.0, cbar=True, yticklabels=False, xticklabels=False)
        axs[pid][did].title.set_text(d+"_"+models[pid]) 
        axs[pid][did].tick_params(left=False, bottom=False)

plt.savefig('heatmap.png')
#plt.show()
