import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def extract_csv_gen_plot(csv_path):

#    data = pd.read_csv(csv_path, header=None)
    data = pd.read_csv(csv_path,float_precision='round_trip',header=None)
    data = data.iloc[:,2]
    df2 = pd.DataFrame(index=range(625),columns=range(625),dtype=np.float64)
    df2 = df2.iloc[1:]
    #df2.index = df2.index + 1


    idx = 0

    for i in range(1, 625):
        for n in range(1,625):
#            print(i,n,data[idx])
            df2[n][i] = data[idx]
            idx = idx + 1

    print(df2)
#    data = data.drop(data.columns[[0]], axis=1)
#    print(data)
#    df2.index.names = ['Code Region']
    g = sns.heatmap(df2,cmap="rocket_r")
#    g = sns.heatmap(data,cmap="PiYG",annot=True, vmin = 0.7, vmax = 1.0)
    g.set_yticklabels(g.get_yticklabels(), rotation=0)
    g.set_title('Heatmap')
#    plt.tight_layout()
#    plt.show()
    g.figure.savefig("heatmap.png")


extract_csv_gen_plot("cosine_similarity_DRB.csv")
