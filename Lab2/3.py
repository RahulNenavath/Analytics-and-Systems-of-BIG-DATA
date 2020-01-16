# 3rd Question:

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


water = [3.2, 3.5, 3.6, 2.5, 2.8, 5.9, 2.9, 3.9, 4.9, 6.9, 7.9, 8.0, 3.3, 6.6, 4.4]
baverages = [2.2, 2.5, 2.6, 1.5, 3.8, 1.9, 0.9, 3.9, 4.9, 6.9, 0.1, 8.0, 0.3, 2.6, 1.4]

data = {'Water':water, 'Baverages':baverages}

df3 = pd.DataFrame(data)

mean_w = df3['Water'].mean()
mean_b = df3['Baverages'].mean()

median_w =  df3['Water'].median()
median_b = df3['Baverages'].median()

mode_w = df3['Water'].mode()[0]
mode_b = df3['Baverages'].mode()[0]

f, ax_hist = plt.subplots(1)

# Density plot:

sns.kdeplot(df3['Water'], color='r', ax=ax_hist, shade=True)
sns.kdeplot(df3['Baverages'], color='g', ax=ax_hist, shade=True)

plt.axvline(mean_w, color='r', linestyle='--')
plt.axvline(mean_b, color='g', linestyle='--')

plt.axvline(median_w, color='r')
plt.axvline(median_b, color='g')

plt.axvline(mode_w, color='r', linestyle=':')
plt.axvline(mode_b, color='g', linestyle=':')


plt.legend({'Mean Water': mean_w, 'Mean Baverage': mean_b, 'Median Water': median_w,'Median Baverage': median_b, 'Mode Water':mode_w, 'Mode Baverage':mode_b})

# Rug plot:

sns.rugplot(df3['Water'], color='r')
sns.rugplot(df3['Baverages'], color='b')

# positive skewness is present in the distribution of water and baverages. Mode is same for both.

plt.show()