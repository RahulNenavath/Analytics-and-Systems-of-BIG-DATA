import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


height = [167.65, 167, 172, 175, 165, 167, 168, 167, 167.3, 170, 167.5, 170, 167, 169, 172]

data = {'Height':height}

df4 = pd.DataFrame(data)

sns.boxplot(df4['Height']) # Box plot for 5 point sumary of data


df4.describe() # For Summary Stats

mean = df4['Height'].mean()
median = df4['Height'].median()
mode = df4['Height'].mode()[0]
std = df4['Height'].std()
Skewness_measure = ( (mean - mode) / std )

# Plot representing the height data (Mean, Median, Mode)

f, ax_hist = plt.subplots(1)

sns.distplot(df4['Height'], ax=ax_hist, bins=10)

plt.axvline(mean, color='r', linestyle='--')
plt.axvline(median, color='g',linestyle='--' )
plt.axvline(mode, color='b', linestyle='--')

plt.legend({'Mean':mean,'Median':median,'Mode':mode})

plt.show()