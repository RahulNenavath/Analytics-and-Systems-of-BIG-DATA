# 7th Question:

from math import pi
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

shop = ['Textile','Jewellery','Cleaning Essentials','Cosmetics']
Q1 = [10,5,15,14]
Q2 = [6,5,20,10]
Q3 = [8,2,16,21]
Q4 = [13,4,15,11]

data = {'Shop Category': shop, 'Quarter 1':Q1, 'Quarter 2':Q2, 'Quarter 3':Q3, 'Quarter 4':Q4}

df7 = pd.DataFrame(data)

df7 = df7.set_index('Shop Category') 


categories = list(df7)

labels=np.array(categories)
stats=df7.loc[:,labels].values

angles=np.linspace(0, 2*np.pi, len(labels), endpoint=False)
# close the plot
stats=np.concatenate((stats,[stats[0]]))
angles=np.concatenate((angles,[angles[0]]))


fig=plt.figure()
ax = fig.add_subplot(111, polar=True)
ax.plot(angles, stats, 'o-', linewidth=2)
ax.fill(angles, stats, alpha=0.25)
ax.set_thetagrids(angles * 180/np.pi, labels)
plt.legend(['Textile','Jewellery','Cleaning Essentials','Cosmetics'])
ax.grid(True)

plt.show()
