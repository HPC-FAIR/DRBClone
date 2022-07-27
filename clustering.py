import numpy as np 
import os 
import matplotlib
import matplotlib.pyplot as plt
import sys


from sklearn.cluster import MiniBatchKMeans 
from sklearn.cluster import AgglomerativeClustering
import scipy.cluster.hierarchy as shc 


def plot_matrix(m): 
    
    

    plt.matshow(m)
    plt.savefig('temp.png')


def dendrogram(mat): 
    
    plt.figure(figsize=(25, 50)) 
    plt.title("Dendrograms") 
    dend = shc.dendrogram(shc.linkage(mat, method='complete')) 
    plt.savefig('dendrogram.png')

    

def clustering(mat): 
    

    model = AgglomerativeClustering(affinity='precomputed', n_clusters=2, linkage='complete')
    model.fit(mat)

    
    print(model.labels_)


def invert_similar(m): 
    # 1 - s 
    # sqrt( 1 - s) 
    # - log(s) 
    # (1/s) -1 
    
    
    return np.array(list(map(lambda s : -np.log(s), m)))


def main(): 
    
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
        # print(label) 
        # print(label.shape)
        mat = data['score']
        print(mat)
        print(mat.max()) 
        print(mat.min())
        # print(mat.shape)

        
        dist = invert_similar(mat)
        print(dist)
        print(dist.max())
        print(dist.min())
        plot_matrix(dist) 
        
        dendrogram(mat)
        clustering(dist) 





if __name__ == "__main__": 
    main()
