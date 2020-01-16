#6th Question:

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

mu, sigma = 0,0.1

std = np.random.normal(mu,sigma,1000)
log = np.random.lognormal(mu, sigma, 1000)

normal_dist = list(std)
log_normal = list(log)

data = {'Normal Distribution': normal_dist, 'Log Normal Distribution': log_normal}

df6 = pd.DataFrame(data)

mean = df6['Normal Distribution'].mean()
median = df6['Normal Distribution'].median()

mean_log = df6['Log Normal Distribution'].mean()
median_log = df6['Log Normal Distribution'].median()

f, ax_hist = plt.subplots(1)

sns.distplot(normal_dist, ax=ax_hist)
sns.violinplot(df6['Normal Distribution'])

plt.axvline(mean, color='r', linestyle='--')
plt.axvline(median, color='g', linestyle='--')

plt.legend({'Mean':mean, 'Median':median})

sns.distplot(df6['Log Normal Distribution'], ax=ax_hist)
sns.violinplot(df6['Log Normal Distribution'])

plt.axvline(mean_log, color='r', linestyle='--')
plt.axvline(median_log, color='g', linestyle='--')

plt.legend({'Mean':mean_log,'Median':median_log})

plt.show()