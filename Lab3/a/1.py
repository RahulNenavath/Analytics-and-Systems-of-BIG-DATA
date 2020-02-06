import pandas as pd
from sklearn.preprocessing import MinMaxScaler, StandardScaler


age = [13, 15, 16, 16, 19, 20, 20, 21, 22, 22, 25, 25, 25, 25, 30, 33, 33, 35, 35, 35, 35, 36, 40, 45, 46, 52, 70]
data = {'Age':age}
df1 = pd.DataFrame(data)

minMax_scalar = MinMaxScaler()
x = minMax_scalar.fit_transform(df1)
minMax_df = pd.DataFrame(x,columns=['Age'])

std_scalar = StandardScaler()
y = std_scalar.fit_transform(df1)
z_score_scalar = pd.DataFrame(y, columns=['Age'])

max_ = df1['Age'].max()

for j in range(1,4):
  if (max_ // 10**j == 0):
    break
  else:
    continue

list_ = []
for i in df1['Age']:
  h = i / 10**j
  list_.append(h)

decimal_scalar = pd.DataFrame({'Age':list_})

print('Min Max Scalar:')
print()
print(minMax_df.head())
print('----------------')
print('Z Score Scalar:')
print()
print(z_score_scalar.head())
print('----------------')
print('Decimal Scalar:')
print()
print(decimal_scalar.head())
print('----------------')