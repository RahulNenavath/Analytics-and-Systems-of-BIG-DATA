import pandas as pd
import matplotlib.pyplot as plt

data = {'Activities':['Studying','Sleeping','Playing','Hobbies'], 'Weightage':[0.33,0.30,0.18,0.19]}

df6 = pd.DataFrame(data)

sums = df6.Weightage.groupby(df6.Activities).sum()
plt.axis('equal')
plt.pie(sums,labels=sums.index)
plt.show()