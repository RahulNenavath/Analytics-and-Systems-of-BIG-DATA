import pandas as pd
import statistics as stats


Marks = []
Rollno = []

for i in range(1,19):

  Rollno.append('CSE20D0{}'.format(i))

  if i %2 == 0:
    x = 25+((i+8)%10)
    Marks.append(x)
  else:
    x = 25+((i+7)%10)
    Marks.append(x)


data = {'Roll No': Rollno, 'Marks': Marks  }

df1 = pd.DataFrame(data)

mean = stats.mean(df1['Marks'])

median = stats.median(df1['Marks'])

print(df1)
print('Mean: {} and Median: {}'.format(mean,median))