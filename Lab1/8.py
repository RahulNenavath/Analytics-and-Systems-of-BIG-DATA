import pandas as pd

# Relative grading:

df8 = pd.read_csv('MarksSheet.csv')

df8['Total'] = df8[['MidSem','EndSem','Assignments']].sum(axis=1)

class_average = df8['Total'].mean()

passing_minimum = class_average / 2

pm_sum = 0
pm_count = 0

for i in df8['Total']:
  if i > passing_minimum:
    pm_sum = i + pm_sum
  else:
    pass

for i in df8['Total']:
  if i > passing_minimum:
    pm_count = pm_count + 1
  else:
    pass

passing_students_mean = pm_sum / pm_count

X = passing_students_mean - passing_minimum

max_marks = df8['Total'].max()

S = round(max_marks - 0.1 * (max_marks - passing_students_mean))

Y = round(S - passing_students_mean)

A = round(passing_students_mean + (Y * 5 / 8))

B = round(passing_students_mean + (Y * 2 / 8))

C = round(passing_students_mean - (X * 2 / 8))

D = round(passing_students_mean - (X * 5 / 8))

E = round(passing_minimum)

print('S: {}, A: {}, B: {}, C: {}, D: {}, E: {}'.format(S,A,B,C,D,E))

grades = []

for i in df8['Total']:
  if i >= S:
    grades.append('S')
  elif i >= A and i < S:
    grades.append('A')
  elif i >= B and i < A:
    grades.append('B')
  elif i >= C and i < B:
    grades.append('C')
  elif i >= D and i < C:
    grades.append('D')
  elif i < D or i < E:
    grades.append('E')
  else:
    pass

df8['Grades'] = grades

print(df8)