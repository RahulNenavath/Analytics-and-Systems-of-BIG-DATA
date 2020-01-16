# 9th Question:

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

temp = [98,87,90,85,95,75]
no_of_cust = [15,12,10,10,16,7]

data = {'Temperature': temp, 'No of Customers':no_of_cust}

df9 = pd.DataFrame(data)

correlation = df9.corr()

print(correlation)

sns.regplot(x='Temperature', y='No of Customers', data=df9)

print('Positive correlation, i.e as the climate gets warmer, the number of Customers increases')

plt.show()