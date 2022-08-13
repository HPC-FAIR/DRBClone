#Reference: https://github.com/hadrienj/Preprocessing-for-deep-learning

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def center(X):
    newX = X - np.mean(X, axis = 0)
    return newX

def standardize(X):
    newX = center(X)/np.std(X, axis = 0)
    return newX

def plotDataAndCov(data, axinput):
    ACov = np.cov(data, rowvar=False, bias=True)
    print ('Covariance matrix:\n', ACov)

#    fig, ax = plt.subplots(nrows=1, ncols=2)
#    fig.set_size_inches(10, 10)

#    ax0 = plt.subplot(2, 2, 1)

    # Choosing the colors
    cmap = sns.color_palette("GnBu", 10)
    sns.heatmap(ACov, cmap=cmap, ax=axinput, vmin=0)

#    ax1 = plt.subplot(2, 2, 2)
#
#    # data can include the colors
#    if data.shape[1]==3:
#        c=data[:,2]
#    else:
#        c="#0A98BE"
#    ax1.scatter(data[:,0], data[:,1], c=c, s=40)
#
#    # Remove the top and right axes from the data plot
#    ax1.spines['right'].set_visible(False)
#    ax1.spines['top'].set_visible(False)


def convert2D(data, length):
   newdf = pd.DataFrame(index=range(length),columns=range(length),dtype=np.float64)
   idx = 0
   for i in range(0, length):
       for j in range(0, length):
           newdf.loc[i,j] = data[2][idx]
           idx = idx + 1
   return newdf;         

csv1="cosine_similarity_distanceBase.csv"
csv2="cosine_similarity_codeBERT.csv"
csv3="cosine_similarity_POJ.csv"
csv4="cosine_similarity_DRB.csv"

# model 1: distanceBased
d1 = pd.read_csv(csv1,float_precision='round_trip',header=None)
len1 = len(d1[0].unique())
df1 = convert2D(d1,len1)
##print(df1) 


#model 2: vanilla bert
d2 = pd.read_csv(csv2,float_precision='round_trip',header=None)
len2 = len(d2[0].unique())
df2 = convert2D(d2,len2)

#model 3: POJ bert
d3 = pd.read_csv(csv3,float_precision='round_trip',header=None)
len3 = len(d3[0].unique())
df3 = convert2D(d3,len3)

#model 4: DRB bert
d4 = pd.read_csv(csv4,float_precision='round_trip',header=None)
len4 = len(d4[0].unique())
df4 = convert2D(d4,len4)
#
##print(len1,len2,len3,len4)
#

fig, (ax1, ax2, ax3, ax4) = plt.subplots(1,4,figsize=(18,4), gridspec_kw={'width_ratios': [10,10,10,11]})

d1Stand = standardize(df1.to_numpy())
d2Stand = standardize(df2.to_numpy())
d3Stand = standardize(df3.to_numpy())
d4Stand = standardize(df4.to_numpy())

plotDataAndCov(d1Stand, ax1)
plotDataAndCov(d2Stand, ax2)
plotDataAndCov(d3Stand, ax3)
plotDataAndCov(d4Stand, ax4)

ax1.title.set_text('Distance-based')
ax2.title.set_text('CodeBERT (M1)')
ax3.title.set_text('POJ-BERT (M2)')
ax4.title.set_text('DRB-BERT (M3)')


#plt.show()
plt.savefig('Covariance.png')
plt.close()

#fig, (ax1, ax2, ax3, ax4) = plt.subplots(1,4,figsize=(18,4), gridspec_kw={'width_ratios': [10,10,10,10]})
##fig.subplots_adjust(wspace=0.01)
#
##sns.heatmap( d1, cmap="rocket_r",ax=ax1)
##sns.heatmap(df2, cmap="rocket_r",ax=ax2)
##sns.heatmap(df3, cmap="rocket_r",ax=ax3)
##sns.heatmap(df4, cmap="rocket_r",ax=ax4)
#
#sns.histplot(d1[2][:], ax = ax1)
#sns.histplot(d2[2][:], ax = ax2)
#sns.histplot(d3[2][:], ax = ax3)
#sns.histplot(d4[2][:], ax = ax4)
#
#ax1.title.set_text('Distance-based')
#ax2.title.set_text('CodeBERT (M1)')
#ax3.title.set_text('POJ-BERT (M2)')
#ax4.title.set_text('DRB-BERT (M3)')
#
#plt.show() 
