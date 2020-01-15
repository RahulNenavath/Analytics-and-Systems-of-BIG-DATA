import pandas as pd
import statistics as stats
import random as rnd 
import seaborn as sns
import matplotlib.pyplot as plt

X = Y =  []

for i in range(0,20):

  x = rnd.randrange(10,100)
  y = 2*x + 3

  X.append(x)
  Y.append(y)

data = {'X':X, 'Y':Y}

df2 = pd.DataFrame(data)



std_y = stats.stdev(df2['Y'])


print('Standard Deviation of the Sample: {}'.format(std_y))


df2.plot.scatter(x='X', y='Y')

sns.distplot(df2['Y'])

plt.show()