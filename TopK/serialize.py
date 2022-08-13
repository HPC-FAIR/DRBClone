import pandas as pd
import numpy as np

data = pd.read_csv("cosine_similarity_distanceBase.csv",float_precision='round_trip',header=None)
print(data)
file1 = open('serialized_DRB_cosineSim.txt', 'w')

for i in range(1,654):
    for j in range(1, 654):
        file1.write(data[i][0]+","+data[0][j]+","+data[i][j]+"\n")


file1.close()
