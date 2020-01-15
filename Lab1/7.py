import pandas as pd

# Absolute grading:

df7 = pd.read_csv('MarksSheet.csv')

df7['Total'] = df7[['MidSem','EndSem','Assignments']].sum(axis=1)

grades = []

class_average = df7['Total'].mean()

E = class_average / 2

for i in df7['Total']:
  if i >= 90:
    grades.append('S')
  elif i >= 80 and i < 90:
    grades.append('A')
  elif i >= 70 and i < 80:
    grades.append('B')
  elif i >= 60 and i < 70:
    grades.append('C')
  elif i >= E and i < 60:
    grades.append('D')
  elif i < E:
    grades.append('E')
  else:
    pass

df7['Grade'] = grades

Freq_table = pd.crosstab(index=df7['Grade'], columns='Count')

print(df7)

print('Frequency Table for the Grades obtained: ')
print(Freq_table)