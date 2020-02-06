import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler, StandardScaler, OneHotEncoder
import seaborn as sns
import statistics as stats
from datetime import datetime
from scipy.stats import entropy
import statsmodels.api as sm 
from collections import Counter 

df2 = pd.read_csv('avocado.csv')
W = df2[['Total Volume', '4046', '4225', '4770', 'type']].where(df2['type']=='organic')

W.dropna(axis=0, inplace=True)

print('\n')
print(W.head())
print('\n')
df3 = pd.read_csv('Trail.csv')

print('length before removing duplicates: {}\n'.format(len(df3)))
df3.drop_duplicates(inplace=True)
print('length after removing duplicates: {}\n'.format(len(df3)))


print('Null values before cleaning: \n')
print(df3.isnull().sum())

df3.fillna(1.25, inplace=True)

print('Null values after cleaning: \n')
print(df3.isnull().sum())

df2['Date_bin']=pd.cut(x=df2['year'], bins=[2015,2016,2017,2018], labels=[1,2,3])
print('\n')
print('Binarized the attribute "year" with threshold of 2016\n')
print(df2.head())
print(df2.tail())

U = df2.copy(deep=True)
U['type']=U['type'].map({'conventional':0,'organic':1})

U['region'].unique()
U['region']=U['region'].map({'Albany':0,'Atlanta':1,'BaltimoreWashington':2, 
        'Boise':3,'Boston':4,'BuffaloRochester':5,'California':6,'Charlotte':7,
        'Chicago':8,'CincinnatiDayton':9,'Columbus':10,'DallasFtWorth':11,'Denver':12,
        'Detroit':13,'GrandRapids':14,'GreatLakes':15,'HarrisburgScranton':16,'HartfordSpringfield':17,
        'Houston':18,'Indianapolis':19,'Jacksonville':20,'LasVegas':21, 'LosAngeles':22, 
        'Louisville':23, 'MiamiFtLauderdale':24,'Midsouth':25, 'Nashville':26, 
        'NewOrleansMobile':27, 'NewYork':28,
       'Northeast':29, 'NorthernNewEngland':30, 'Orlando':31, 'Philadelphia':32,
       'PhoenixTucson':33, 'Pittsburgh':34, 'Plains':35, 'Portland':36,
       'RaleighGreensboro':37, 'RichmondNorfolk':38, 'Roanoke':39, 'Sacramento':40,
       'SanDiego':41, 'SanFrancisco':42, 'Seattle':43, 'SouthCarolina':44,
       'SouthCentral':45, 'Southeast':46, 'Spokane':47, 'StLouis':48, 'Syracuse':49,
       'Tampa':50, 'TotalUS':51, 'West':52, 'WestTexNewMexico':53})
print('\n')
print('Integer Encoding of all Categorical attributes\n')
print(U.head())
print('\n')
print(U.tail())
print('\n')


print('OneHot Encoding of all Categorical attributes\n')
R = pd.get_dummies(df2['region'],drop_first=True)
print(R.head())

print('\n')
print('Before Dropping all the NAN values \n')
print(df2.isnull().sum())
T = df2.dropna()
print('Before Dropping all the NAN values \n')
print(T.isnull().sum())

T.drop('Unnamed: 0', axis=1, inplace=True)

print('\n')
print('Dimensions of the Dataset: {} \n'.format(T.shape))

print('Summary Stats of the Dataset: \n')

print('Most Frequent occuring value in Categorical Attributes: \n')
print(T['type'].value_counts())
print('\n')

print(T['region'].value_counts())
print('\n')

T_num = T[['AveragePrice', 'Total Volume', '4046', '4225', '4770','Total Bags', 'Small Bags', 'Large Bags', 'XLarge Bags','year']]

list_numFreq = []
x = list(T_num.columns)

try:
	for i in range(len(T_num)):
		n_num = list(T_num[x[i]])
		n = len(n_num)
		data = Counter(n_num)
		get_mode = dict(data)
		mode = [k for k, v in get_mode.items() if v == max(list(data.values()))]

		if len(mode) == n:
			get_mode = 0
		else:
			get_mode = mode

		list_numFreq.append(get_mode)

except IndexError:
	pass

print('Most Frequent occuring value in Numerical Attributes: \n')
print(list_numFreq)

print('\n')
print('Datatype of each attribute:')
print(T.info())

print('\n')
print('Stats describe: \n')
print(T.describe())

print('\n')
print('Correlation: \n')
corr = T.corr()
print(corr)
sns.heatmap(corr, xticklabels=corr.columns,yticklabels=corr.columns)
plt.show()

x = list(T_num.columns)

try:
	for i in range(len(T_num)):
		mean = T_num[x[i]].mean()
		median = T_num[x[i]].median()

		fig, ax_hist = plt.subplots(1)
		sns.distplot(T_num[x[i]], bins=20, ax=ax_hist)
		plt.axvline(mean, color='r', linestyle='--')
		plt.axvline(median, color='g', linestyle='--')

		plt.legend({'Mean':mean, 'Median':median})

		plt.show()
except IndexError:
	pass
data = pd.DataFrame({"toothed":["True","True","True","False","True","True","True","True","True","False"],
                     "hair":["True","True","False","True","True","True","False","False","True","False"],
                     "breathes":["True","True","True","True","True","True","False","True","True","True"],
                     "legs":["True","True","False","True","True","True","False","False","True","True"],
                     "species":["Mammal","Mammal","Reptile","Mammal","Mammal","Mammal","Reptile","Reptile","Mammal","Reptile"]}, 
                    columns=["toothed","hair","breathes","legs","species"])

data['species'] = data['species'].map({'Mammal':0,'Reptile':1})

print('\n')
print('New Appropriate dataset for Gini Index and Entropy\n')
print(data)

ctr_1, ctr_2 = 0,0

for i in range(len(data['species'])):
	if data['species'][i] == 0:
		ctr_1 = ctr_1 + 1
	else:
		ctr_2 = ctr_2 + 1

x = ctr_1+ctr_2

pb1 = ctr_1/x
pb2 = ctr_2/x

print('\n')
print('Entropy: {}\n'.format(entropy([pb1,pb2],base=2)))

def gini(list_of_values):
	sorted_list = sorted(list_of_values)
	height, area = 0, 0
	for value in sorted_list:
		height += value
		area += height - value / 2.
	fair_area = height * len(list_of_values) / 2.
	return (fair_area - area) / fair_area

print('\n')
print('Gini Index: {} \n'.format(gini(data['species'])))
  