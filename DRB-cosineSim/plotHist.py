import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns




df = pd.read_csv('OMP-unseen-test/cosine_similarity__NPB-IS-1.csv')

sns.histplot(data=df) 
plt.show() 