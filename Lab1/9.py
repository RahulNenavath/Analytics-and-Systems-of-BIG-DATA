# 9th Question:

import seaborn as sns
import matplotlib.pyplot as plt
from scipy import stats as spyStats

data = [79,71,89,57,76,64,82,82,67,80,81,65,73,79,79,60,58,83,74,68,78,80,78,81,76,65,70,76,58,82,59,73,72,79,87,63,74,90,69,70,83,76,61,66,71,60,57,81,57,65,81,78,77,81,81,63,71,66,56,62,75,64,74,74,70,71,56,69,63,72,81,54,72,91,92]

sns.distplot(data, bins=10) # kernal estimation with histogram

sns.distplot(data, bins=10, kde=False, rug=True) # just histogram

sns.kdeplot(data, shade=True) # just kernal plot of the histogram

sns.distplot(data, fit=spyStats.gamma) # parametric distribution to a dataset and visually evaluate how closely it corresponds to the observed data

plt.show()