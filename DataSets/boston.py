import numpy as np
import pandas as pd
from sklearn import datasets
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')
import matplotlib.pyplot as plt

boston = datasets.load_boston()
df = pd.DataFrame(boston.data, columns = boston.feature_names)
df['MEDV'] = pd.Series(boston.target)
print(df.head())
print(" ")
print("Statistical Information: ")
print(df.describe())
print(' ')
print('Data Type info: ')
print(df.info())
print(' ')
print("Pre-processing: check for null values: ")
print(df.isnull().sum())
print(' ')
print("Exploratory Data Analysis: ")
print("Creating box plots : ")

fig, ax = plt.subplots(ncols = 7, nrows = 2, figsize = (20,10))
index = 0
ax = ax.flatten()
for col, values in df.items():
 sns.boxplot(y = col, data = df, ax = ax[index])
 index += 1

plt.tight_layout(pad = 0.5, w_pad = 0.7, h_pad = 5.0)
#plt.show()

print(' ')
print("Creating Dist plots: ")

fig, ax = plt.subplots(ncols = 7, nrows = 2, figsize = (20,10))
index = 0
ax = ax.flatten()
for col, value in df.items():
 sns.distplot(value, ax = ax[index])
 index += 1

# plt.show()