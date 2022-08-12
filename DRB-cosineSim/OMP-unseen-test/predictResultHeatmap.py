import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from matplotlib.patches import Rectangle


-rw-r--r--  1 lin32  42876  39020 Aug 12 12:18 cosine_similarity_DRB_NPB-IS-1.csv
-rw-r--r--  1 lin32  42876  38991 Aug 12 12:18 cosine_similarity_DRB_NPB-IS-2.csv
-rw-r--r--  1 lin32  42876  43378 Aug 12 12:18 cosine_similarity_DRB_rodinia-bfs-1.csv
-rw-r--r--  1 lin32  42876  50242 Aug 12 12:18 cosine_similarity_DRB_rodinia-hotspot_openmp-1.csv
-rw-r--r--  1 lin32  42876  43982 Aug 12 12:18 cosine_similarity_DRB_rodinia-lud_omp-1.csv
-rw-r--r--  1 lin32  42876  45912 Aug 12 12:18 cosine_similarity_DRB_rodinia-nn_openmp-1.csv
-rw-r--r--  1 lin32  42876  55821 Aug 12 12:18 cosine_similarity_N_NPB-IS-2.csv
-rw-r--r--  1 lin32  42876  38994 Aug 12 12:18 cosine_similarity_POJ_NPB-IS-1.csv
-rw-r--r--  1 lin32  42876  39010 Aug 12 12:18 cosine_similarity_POJ_NPB-IS-2.csv
-rw-r--r--  1 lin32  42876  43390 Aug 12 12:18 cosine_similarity_POJ_rodinia-bfs-1.csv
-rw-r--r--  1 lin32  42876  50213 Aug 12 12:18 cosine_similarity_POJ_rodinia-hotspot_openmp-1.csv
-rw-r--r--  1 lin32  42876  43974 Aug 12 12:18 cosine_similarity_POJ_rodinia-lud_omp-1.csv
-rw-r--r--  1 lin32  42876  45798 Aug 12 12:18 cosine_similarity_POJ_rodinia-nn_openmp-1.csv
-rw-r--r--  1 lin32  42876  39563 Aug 12 12:18 cosine_similarity__NPB-IS-1.csv
-rw-r--r--  1 lin32  42876  39588 Aug 12 12:18 cosine_similarity__NPB-IS-2.csv
-rw-r--r--  1 lin32  42876  43813 Aug 12 12:18 cosine_similarity__rodinia-bfs-1.csv
-rw-r--r--  1 lin32  42876  50584 Aug 12 12:18 cosine_similarity__rodinia-hotspot_openmp-1.csv
-rw-r--r--  1 lin32  42876  44586 Aug 12 12:18 cosine_similarity__rodinia-lud_omp-1.csv
-rw-r--r--  1 lin32  42876  46362 Aug 12 12:18 cosine_similarity__rodinia-nn_openmp-1.csv


def convert(l):
    df2 = pd.DataFrame(index=range(625),columns=range(625),dtype=np.float64)
    df2 = df2.iloc[1:]
    idx = 0
    for i in range(1, 625):
        for n in range(1,625):
#            print(i,n,l[idx])
            df2[n][i] = l[idx]
            idx = idx + 1
    return df2

csv1="cosine_similarity_distanceBase.csv"
csv2="cosine_similarity_codeBERT.csv"
csv3="cosine_similarity_POJ.csv"
csv4="cosine_similarity_DRB.csv"

# model 1: distanceBased
d1 = pd.read_csv(csv1,float_precision='round_trip',header=None)
d1 = d1.apply(pd.to_numeric, errors='coerce')
d1 = d1.iloc[1:]
d1 = d1.drop(d1.columns[[0]], axis=1)
d1.index.names = ['Code Region']

#model 2: vanilla bert
d2 = pd.read_csv(csv2,float_precision='round_trip',header=None)
d2 = d2.iloc[:,2]

df2 = convert(d2) 
#print(df2)

#model 3: POJ bert
d3 = pd.read_csv(csv3,float_precision='round_trip',header=None)
d3 = d3.iloc[:,2]

df3 = convert(d3) 
#print(df3)

#model 4: DRB bert
d4 = pd.read_csv(csv4,float_precision='round_trip',header=None)
d4 = d4.iloc[:,2]

df4 = convert(d4) 
#print(df4)

#plt.rcParams["figure.figsize"] = [16.0, 4.00]
#plt.rcParams["figure.autolayout"] = True

fig, (ax1, ax2, ax3, ax4) = plt.subplots(1,4,figsize=(18,4), gridspec_kw={'width_ratios': [10,10,10,11]})
#fig.subplots_adjust(wspace=0.01)

#sns.heatmap( d1, cmap="rocket_r",ax=ax1)
#sns.heatmap(df2, cmap="rocket_r",ax=ax2)
#sns.heatmap(df3, cmap="rocket_r",ax=ax3)
#sns.heatmap(df4, cmap="rocket_r",ax=ax4)

sns.heatmap( d1, cmap="rocket_r", ax=ax1,  vmin= 0., vmax=1.0, cbar=False)
sns.heatmap(df2, cmap="rocket_r", ax=ax2,  vmin= 0., vmax=1.0, cbar=False)
sns.heatmap(df3, cmap="rocket_r", ax=ax3,  vmin= 0., vmax=1.0, cbar=False)
sns.heatmap(df4, cmap="rocket_r", ax=ax4,  vmin= 0., vmax=1.0, cbar=True)

ax1.title.set_text('Distance-based')
ax2.title.set_text('CodeBERT (M1)')
ax3.title.set_text('POJ-BERT (M2)')
ax4.title.set_text('DRB-BERT (M3)')


#ax4.add_patch(Rectangle((3, 4), 1, 1, fill=False, edgecolor='blue', lw=3))


#fig.subplots_adjust(wspace=0.001)
plt.savefig('heatmap.png')
plt.show()
##    data = pd.read_csv(csv_path, header=None)
#    data = pd.read_csv(csv_path,float_precision='round_trip',header=None)
#    data = data.iloc[:,2]
#    df2 = pd.DataFrame(index=range(625),columns=range(625),dtype=np.float64)
#    df2 = df2.iloc[1:]
#    #df2.index = df2.index + 1
#
#
#    idx = 0
#
#    for i in range(1, 625):
#        for n in range(1,625):
##            print(i,n,data[idx])
#            df2[n][i] = data[idx]
#            idx = idx + 1
#
#    print(df2)
##    data = data.drop(data.columns[[0]], axis=1)
##    print(data)
##    df2.index.names = ['Code Region']
#    g = sns.heatmap(df2,cmap="rocket_r")
##    g = sns.heatmap(data,cmap="PiYG",annot=True, vmin = 0.7, vmax = 1.0)
#    g.set_yticklabels(g.get_yticklabels(), rotation=0)
#    g.set_title('Heatmap')
##    plt.tight_layout()
##    plt.show()
#    g.figure.savefig("heatmap.png")
#
#
#extract_csv_gen_plot("cosine_similarity_DRB.csv")
