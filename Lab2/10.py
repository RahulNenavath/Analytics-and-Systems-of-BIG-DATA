import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


x = np.linspace(25,50,100)
y = np.linspace(10,50,100)

data = {'Age':x, 'Accidents per driver':y}

df10 = pd.DataFrame(data)

plt.hexbin(x='Age', y='Accidents per driver', data=df10)

plt.show()