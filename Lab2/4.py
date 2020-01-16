# 4th Question:

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


fuel = [3.6,6.7,9.8,11.2,14.7]
mass = [0.45,0.91,1.36,1.81,2.27]

data = {'Fuel':fuel,'Mass':mass}

df4 = pd.DataFrame(data)

sns.regplot(x='Mass', y='Fuel', data=df4)

correlation = df4.corr()

print(correlation)

plt.show()

# Fuel and Mass are positively correlated, i.e they have linear relationship.