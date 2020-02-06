import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler, StandardScaler, OneHotEncoder
import seaborn as sns
import statistics as stats
from datetime import datetime
from scipy.stats import entropy
import statsmodels.api as sm 

df2 = pd.read_csv('avocado.csv')

print('Summarization of Missing values:')
print()
print('Null Values before cleaning: ')
print()

print(df2.isnull().sum())

mean = df2['AveragePrice'].mean()
median = df2['AveragePrice'].median()

fig, ax_hist = plt.subplots(1)

sns.distplot(df2['AveragePrice'], bins=20, ax=ax_hist)

plt.axvline(mean, color='r', linestyle='--')
plt.axvline(median, color='g', linestyle='--')

#plt.show()

print('Null Values after cleaning: ')
print()

df2['AveragePrice'].fillna(mean,inplace=True)

print(df2.isnull().sum())

TV_sorted = sorted(df2['Total Volume'])
tv = pd.DataFrame({'TV':TV_sorted})
tv = tv.sort_values(by='TV')

list_ = []
for i in range(len(df2['Date'])):
	x = datetime.strptime(df2['Date'][i], '%m/%d/%Y')
	x = x.month
	list_.append(x)

df2['month'] = list_

# Bin size 50:

bin_50 = []
l = 0

for i in range(int(len(TV_sorted)/50)):
	list_ = []
	for j in range(0,50):
		list_.append(TV_sorted[l+j])
	l = l + 50
	bin_50.append(list_)

# Bin size 250:

bin_250 = []
l = 0

for i in range(int(len(TV_sorted)/250)):
	list_ = []
	for j in range(0,250):
		list_.append(TV_sorted[l+j])
	l = l + 250
	bin_250.append(list_)

# mean, median, boundary for bin of size 50:

bin_50mean = []
bin_50median = []
bin_50boundary = []

for i in range(len(bin_50)):
	list_ = []
	x = stats.mean(bin_50[i])
	for j in range(0,50):
		list_.append(x)
	bin_50mean.append(list_)

for i in range(len(bin_50)):
	list_ = []
	x = stats.median(bin_50[i])
	for j in range(0,50):
		list_.append(x)
	bin_50median.append(list_)


for i in range(len(bin_50)):
	list_ = []
	for j in range(0,50):
		min_ = min(bin_50[i])
		max_ = max(bin_50[i])
		if (bin_50[i][j] <= bin_50median[i][0]):
			list_.append(min_)
		else:
			list_.append(max_)
	bin_50boundary.append(list_)

# mean, median, boundary for bin of size 250:

bin_250mean = []
bin_250median = []
bin_250boundary = []

for i in range(len(bin_250)):
	list_ = []
	x = stats.mean(bin_250[i])
	for j in range(0,250):
		list_.append(x)
	bin_250mean.append(list_)

for i in range(len(bin_250)):
	list_ = []
	x = stats.median(bin_250[i])
	for j in range(0,250):
		list_.append(x)
	bin_250median.append(list_)


for i in range(len(bin_250)):
	list_ = []
	for j in range(0,250):
		min_ = min(bin_250[i])
		max_ = max(bin_250[i])
		if (bin_250[i][j] <= bin_250median[i][0]):
			list_.append(min_)
		else:
			list_.append(max_)
	bin_250boundary.append(list_)

print('Bin Mean for bin size 50\n')
print(bin_50mean[5])
print('Bin Median for bin size 50\n')
print(bin_50median[1])
print('Bin boundary for bin size 50\n')
print(bin_50boundary[7])
print('\n')
print('Bin Mean for bin size 250\n')
print(bin_250mean[3])
print('Bin Median for bin size 250\n')
print(bin_250median[9])
print('Bin boundary for bin size 250\n')
print(bin_250boundary[1])

Y = df2.sort_values(by='year', ascending=True)
Y = Y.drop(columns=['Unnamed: 0'] ,axis=1)
Y = Y.drop(columns=['Date','Total Bags','Small Bags','Large Bags','XLarge Bags','type','region'] ,axis=1)

Y2015 = Y[['AveragePrice','4046','4225','4770']].where(Y['year'] == 2015)
Y2015.dropna(axis=0, inplace=True)
Y2015['Avg Price per no of 4046 sold'] = Y2015['AveragePrice']*Y2015['4046']
Y2015['Avg Price per no of 4225 sold'] = Y2015['AveragePrice']*Y2015['4225']
Y2015['Avg Price per no of 4770 sold'] = Y2015['AveragePrice']*Y2015['4770']

Y2016 = Y[['AveragePrice','4046','4225','4770']].where(Y['year'] == 2016)
Y2016.dropna(axis=0, inplace=True)
Y2016['Avg Price per no of 4046 sold'] = Y2016['AveragePrice']*Y2016['4046']
Y2016['Avg Price per no of 4225 sold'] = Y2016['AveragePrice']*Y2016['4225']
Y2016['Avg Price per no of 4770 sold'] = Y2016['AveragePrice']*Y2016['4770']

Y2017 = Y[['AveragePrice','4046','4225','4770']].where(Y['year'] == 2017)
Y2017.dropna(axis=0, inplace=True)
Y2017['Avg Price per no of 4046 sold'] = Y2017['AveragePrice']*Y2017['4046']
Y2017['Avg Price per no of 4225 sold'] = Y2017['AveragePrice']*Y2017['4225']
Y2017['Avg Price per no of 4770 sold'] = Y2017['AveragePrice']*Y2017['4770']

Y2018 = Y[['AveragePrice','4046','4225','4770']].where(Y['year'] == 2018)
Y2018.dropna(axis=0, inplace=True)
Y2018['Avg Price per no of 4046 sold'] = Y2018['AveragePrice']*Y2018['4046']
Y2018['Avg Price per no of 4225 sold'] = Y2018['AveragePrice']*Y2018['4225']
Y2018['Avg Price per no of 4770 sold'] = Y2018['AveragePrice']*Y2018['4770']

list_2015 = [int(sum(Y2015['4046'])),int(sum(Y2015['4225'])),int(sum(Y2015['4770'])),int(sum(Y2015['Avg Price per no of 4046 sold'])),int(sum(Y2015['Avg Price per no of 4225 sold'])),int(sum(Y2015['Avg Price per no of 4770 sold']))]
list_2016 = [int(sum(Y2016['4046'])),int(sum(Y2016['4225'])),int(sum(Y2016['4770'])),int(sum(Y2016['Avg Price per no of 4046 sold'])),int(sum(Y2016['Avg Price per no of 4225 sold'])),int(sum(Y2016['Avg Price per no of 4770 sold']))]
list_2017 = [int(sum(Y2017['4046'])),int(sum(Y2017['4225'])),int(sum(Y2017['4770'])),int(sum(Y2017['Avg Price per no of 4046 sold'])),int(sum(Y2017['Avg Price per no of 4225 sold'])),int(sum(Y2017['Avg Price per no of 4770 sold']))]
list_2018 = [int(sum(Y2018['4046'])),int(sum(Y2018['4225'])),int(sum(Y2018['4770'])),int(sum(Y2018['Avg Price per no of 4046 sold'])),int(sum(Y2018['Avg Price per no of 4225 sold'])),int(sum(Y2018['Avg Price per no of 4770 sold']))]

Total_annual = pd.DataFrame({'2015':list_2015,'2016':list_2016,'2017':list_2017,'2018':list_2018}, index=['Total 4046 sold','Total 4225 sold','Total 4770 sold','Avg Price per no of 4046 sold','Avg Price per no of 4225 sold','Avg Price per no of 4770 sold'])


Z = df2.sort_values(by='month', ascending=True)
Z = Z.drop(columns=['Unnamed: 0'] ,axis=1)
Z = Z.drop(columns=['Date','Total Bags','Small Bags','Large Bags','XLarge Bags','type','year','region',] ,axis=1)

x1 = Z[['AveragePrice','4046','4225','4770']].where(Z['month'] == 1)
x1.dropna(axis=0, inplace=True)
x1['Avg Price per no of 4046 sold'] = x1['AveragePrice']*x1['4046']
x1['Avg Price per no of 4225 sold'] = x1['AveragePrice']*x1['4225']
x1['Avg Price per no of 4770 sold'] = x1['AveragePrice']*x1['4770']

x2 = Z[['AveragePrice','4046','4225','4770']].where(Z['month'] == 2)
x2.dropna(axis=0, inplace=True)
x2['Avg Price per no of 4046 sold'] = x2['AveragePrice']*x2['4046']
x2['Avg Price per no of 4225 sold'] = x2['AveragePrice']*x2['4225']
x2['Avg Price per no of 4770 sold'] = x2['AveragePrice']*x2['4770']

x3 = Z[['AveragePrice','4046','4225','4770']].where(Z['month'] == 3)
x3.dropna(axis=0, inplace=True)
x3['Avg Price per no of 4046 sold'] = x3['AveragePrice']*x3['4046']
x3['Avg Price per no of 4225 sold'] = x3['AveragePrice']*x3['4225']
x3['Avg Price per no of 4770 sold'] = x3['AveragePrice']*x3['4770']

x4 = Z[['AveragePrice','4046','4225','4770']].where(Z['month'] == 4)
x4.dropna(axis=0, inplace=True)
x4['Avg Price per no of 4046 sold'] = x4['AveragePrice']*x4['4046']
x4['Avg Price per no of 4225 sold'] = x4['AveragePrice']*x4['4225']
x4['Avg Price per no of 4770 sold'] = x4['AveragePrice']*x4['4770']

x5 = Z[['AveragePrice','4046','4225','4770']].where(Z['month'] == 5)
x5.dropna(axis=0, inplace=True)
x5['Avg Price per no of 4046 sold'] = x5['AveragePrice']*x5['4046']
x5['Avg Price per no of 4225 sold'] = x5['AveragePrice']*x5['4225']
x5['Avg Price per no of 4770 sold'] = x5['AveragePrice']*x5['4770']

x6 = Z[['AveragePrice','4046','4225','4770']].where(Z['month'] == 6)
x6.dropna(axis=0, inplace=True)
x6['Avg Price per no of 4046 sold'] = x6['AveragePrice']*x6['4046']
x6['Avg Price per no of 4225 sold'] = x6['AveragePrice']*x6['4225']
x6['Avg Price per no of 4770 sold'] = x6['AveragePrice']*x6['4770']

x7 = Z[['AveragePrice','4046','4225','4770']].where(Z['month'] == 7)
x7.dropna(axis=0, inplace=True)
x7['Avg Price per no of 4046 sold'] = x7['AveragePrice']*x7['4046']
x7['Avg Price per no of 4225 sold'] = x7['AveragePrice']*x7['4225']
x7['Avg Price per no of 4770 sold'] = x7['AveragePrice']*x7['4770']

x8 = Z[['AveragePrice','4046','4225','4770']].where(Z['month'] == 8)
x8.dropna(axis=0, inplace=True)
x8['Avg Price per no of 4046 sold'] = x8['AveragePrice']*x8['4046']
x8['Avg Price per no of 4225 sold'] = x8['AveragePrice']*x8['4225']
x8['Avg Price per no of 4770 sold'] = x8['AveragePrice']*x8['4770']

x9 = Z[['AveragePrice','4046','4225','4770']].where(Z['month'] == 9)
x9.dropna(axis=0, inplace=True)
x9['Avg Price per no of 4046 sold'] = x9['AveragePrice']*x9['4046']
x9['Avg Price per no of 4225 sold'] = x9['AveragePrice']*x9['4225']
x9['Avg Price per no of 4770 sold'] = x9['AveragePrice']*x9['4770']

x10 = Z[['AveragePrice','4046','4225','4770']].where(Z['month'] == 10)
x10.dropna(axis=0, inplace=True)
x10['Avg Price per no of 4046 sold'] = x10['AveragePrice']*x10['4046']
x10['Avg Price per no of 4225 sold'] = x10['AveragePrice']*x10['4225']
x10['Avg Price per no of 4770 sold'] = x10['AveragePrice']*x10['4770']

x11 = Z[['AveragePrice','4046','4225','4770']].where(Z['month'] == 11)
x11.dropna(axis=0, inplace=True)
x11['Avg Price per no of 4046 sold'] = x11['AveragePrice']*x11['4046']
x11['Avg Price per no of 4225 sold'] = x11['AveragePrice']*x11['4225']
x11['Avg Price per no of 4770 sold'] = x11['AveragePrice']*x11['4770']

x12 = Z[['AveragePrice','4046','4225','4770']].where(Z['month'] == 12)
x12.dropna(axis=0, inplace=True)
x12['Avg Price per no of 4046 sold'] = x12['AveragePrice']*x12['4046']
x12['Avg Price per no of 4225 sold'] = x12['AveragePrice']*x12['4225']
x12['Avg Price per no of 4770 sold'] = x12['AveragePrice']*x12['4770']

list_1 = [int(sum(x1['4046'])),int(sum(x1['4225'])),int(sum(x1['4770'])),int(sum(x1['Avg Price per no of 4046 sold'])),int(sum(x1['Avg Price per no of 4225 sold'])),int(sum(x1['Avg Price per no of 4770 sold']))]
list_2 = [int(sum(x2['4046'])),int(sum(x2['4225'])),int(sum(x2['4770'])),int(sum(x2['Avg Price per no of 4046 sold'])),int(sum(x2['Avg Price per no of 4225 sold'])),int(sum(x2['Avg Price per no of 4770 sold']))]
list_3 = [int(sum(x3['4046'])),int(sum(x3['4225'])),int(sum(x3['4770'])),int(sum(x3['Avg Price per no of 4046 sold'])),int(sum(x3['Avg Price per no of 4225 sold'])),int(sum(x3['Avg Price per no of 4770 sold']))]
list_4 = [int(sum(x4['4046'])),int(sum(x4['4225'])),int(sum(x4['4770'])),int(sum(x4['Avg Price per no of 4046 sold'])),int(sum(x4['Avg Price per no of 4225 sold'])),int(sum(x4['Avg Price per no of 4770 sold']))]
list_5 = [int(sum(x5['4046'])),int(sum(x5['4225'])),int(sum(x5['4770'])),int(sum(x5['Avg Price per no of 4046 sold'])),int(sum(x5['Avg Price per no of 4225 sold'])),int(sum(x5['Avg Price per no of 4770 sold']))]
list_6 = [int(sum(x6['4046'])),int(sum(x6['4225'])),int(sum(x6['4770'])),int(sum(x6['Avg Price per no of 4046 sold'])),int(sum(x6['Avg Price per no of 4225 sold'])),int(sum(x6['Avg Price per no of 4770 sold']))]
list_7 = [int(sum(x7['4046'])),int(sum(x7['4225'])),int(sum(x7['4770'])),int(sum(x7['Avg Price per no of 4046 sold'])),int(sum(x7['Avg Price per no of 4225 sold'])),int(sum(x7['Avg Price per no of 4770 sold']))]
list_8 = [int(sum(x8['4046'])),int(sum(x8['4225'])),int(sum(x8['4770'])),int(sum(x8['Avg Price per no of 4046 sold'])),int(sum(x8['Avg Price per no of 4225 sold'])),int(sum(x8['Avg Price per no of 4770 sold']))]
list_9 = [int(sum(x9['4046'])),int(sum(x9['4225'])),int(sum(x9['4770'])),int(sum(x9['Avg Price per no of 4046 sold'])),int(sum(x9['Avg Price per no of 4225 sold'])),int(sum(x9['Avg Price per no of 4770 sold']))]
list_10 = [int(sum(x10['4046'])),int(sum(x10['4225'])),int(sum(x10['4770'])),int(sum(x10['Avg Price per no of 4046 sold'])),int(sum(x10['Avg Price per no of 4225 sold'])),int(sum(x10['Avg Price per no of 4770 sold']))]
list_11 = [int(sum(x11['4046'])),int(sum(x11['4225'])),int(sum(x11['4770'])),int(sum(x11['Avg Price per no of 4046 sold'])),int(sum(x11['Avg Price per no of 4225 sold'])),int(sum(x11['Avg Price per no of 4770 sold']))]
list_12 = [int(sum(x12['4046'])),int(sum(x12['4225'])),int(sum(x12['4770'])),int(sum(x12['Avg Price per no of 4046 sold'])),int(sum(x12['Avg Price per no of 4225 sold'])),int(sum(x12['Avg Price per no of 4770 sold']))]

Total_monthly = pd.DataFrame({'January':list_1,'February':list_2,'March':list_3,'April':list_4,'May':list_5 ,'June':list_6, 'July':list_7, 'August':list_8, 'September':list_9,'October':list_10, 'November':list_11, 'December':list_12}, index=['Total 4046 sold','Total 4225 sold','Total 4770 sold','Avg Price per no of 4046 sold','Avg Price per no of 4225 sold','Avg Price per no of 4770 sold'])

print('Monthly Report\n')
print(Total_monthly)

print('Annual Report\n')
print(Total_annual)

X = df2.sort_values(by='Date', ascending=True)
X = X.drop(columns=['Unnamed: 0'] ,axis=1)
X['Date_bin']=pd.cut(x=X['year'], bins=[2014,2015,2016,2017,2018], labels=[0,1,2,3])
#0:"OLD",1:"Old",2:"New",3:"Recent"

sm.qqplot(X['Date_bin'], line ='45')
