import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

grades = []
rollno = []

for i in range(1,101):
  
  rollno.append(i)
  if i in range(1,32):
    grades.append('S')
  
  elif i in range(32,61):
    grades.append('B')

  elif i in range(61,86):
    grades.append('C')

  elif i in range(86,101):
    grades.append('D')

  else:
    pass



data = {'Rollno':rollno,'Grades':grades}
df5 = pd.DataFrame(data)

#sns.barplot(x='Grades', y='Rollno', data=df5)

sums = df5.Rollno.groupby(df5.Grades).sum()
plt.axis('equal');
plt.pie(sums, labels=sums.index);
plt.show()