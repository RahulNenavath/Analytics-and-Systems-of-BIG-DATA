# 1st Question:

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

age = [7, 9, 27, 28, 55, 45, 34, 65, 54, 67, 34, 23, 24, 66, 53, 45, 44, 88, 22, 33, 55, 35, 33, 37, 47, 41,31, 30, 29, 12]

data = {'Age':age}

df1 = pd.DataFrame(data)

mean = df1['Age'].mean()
median = df1['Age'].median()

f,ax_hist = plt.subplots(1)

sns.distplot(df1['Age'], ax=ax_hist, bins=20)

plt.axvline(mean, color='r', linestyle='--')
plt.axvline(median, color='b', linestyle='--')

plt.legend({'Mean: ':mean, 'Median: ':median})

plt.show()

# UniModal (Single peak in the curve/ Single local maxima)
# Skewness (Rightly Skewness)