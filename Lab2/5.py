# 5th Question: 

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

chairs = [35, 54, 60, 65, 66, 67, 69, 70, 72, 73, 75, 76, 54, 25, 15, 60, 65, 66, 67, 69, 70, 72, 130, 73, 75, 76]

data = {'Chairs':chairs}

df5 = pd.DataFrame(data)

sns.boxplot(df5['Chairs'])
sns.swarmplot(df5['Chairs'], color='r')

plt.show()

#outliers: 15,25,35,130