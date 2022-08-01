import numpy as np 
import os 
import matplotlib
import matplotlib.pyplot as plt
import sys


from sklearn.cluster import MiniBatchKMeans 
from sklearn.cluster import AgglomerativeClustering
import scipy.cluster.hierarchy as shc 


def plot_matrix(m, func='original'): 
    
    mat = invert_similar(m, func)

    plt.matshow(mat)
    plt.savefig('graph/heatmap_{}.png'.format(func))


def dendrogram(m, func='original'): 
    
    mat = invert_similar(m, func) 

    plt.figure(figsize=(25, 50)) 
    plt.title("Dendrograms") 
    dend = shc.dendrogram(shc.linkage(mat, method='complete')) 
    plt.savefig('graph/dendrogram_{}.png'.format(func))

    

def clustering(mat, func='original'): 
    
    mat = invert_similar(mat, func) 

    model = AgglomerativeClustering(affinity='precomputed', n_clusters=2, linkage='complete')
    model.fit(mat)

    
    print(model.labels_)


def invert_similar(m, func): 
    # 1 - s 
    # sqrt( 1 - s) 
    # - log(s) 
    # (1/s) -1 
    if func == 'log': 
        return np.array(list(map(lambda s : -np.log(s), m)))
    elif func == 'sqrt': 
        return np.array(list(map(lambda s : sqrt(1-s), m)))
    else: 
        return m 

def main(): 
    
    # reading prediction.txt  
    with open("./saved_models/predictions.txt", 'r') as f: 

        lines = f.readlines() 
        data = []
        dtype = [('func1', 'S6'), ('func2', 'S6'), ('score', float)]
        for line in lines: 
            func1, func2, score = line.split('\t')
            score = score.strip('\n')
           
            data.append(np.array((func1, func2, float(score)), dtype=dtype))
        
        data = np.array(data)
        # print(data.shape)
        data.sort(order=['func1', 'func2', 'score'])
        data.resize(181, 181)
        label = data['func2'][0]
        
        
        mat = data['score']

        plot_matrix(mat) 
        plot_matrix(mat, 'log') 

        dendrogram(mat) 
        dendrogram(mat, 'log') 
        
        clustering(mat, 'log') 





if __name__ == "__main__": 
    main()
