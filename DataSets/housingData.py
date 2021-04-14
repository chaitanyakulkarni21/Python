import numpy as np
import pandas as pd
from sklearn import datasets
import matplotlib.pyplot as plt
import seaborn as sns


boston = datasets.load_boston()
df = pd.DataFrame(boston.data, columns = boston.feature_names)
df['MEDV'] = pd.Series(boston.target)
print("Boston Data set: ")
print(df.head())
print(" ")
print("Shape of Data Set:  ", df.shape)
print("Check if null values present: ")
print(df.isnull().sum())
print("Change MEDV col name to Price: ")

df.rename(columns = {"MEDV" : "PRICE"}, inplace = True)

print(df.head())
print(' ')
print("Exploratory Data Analysis: ")
print(df.info())

print("Describe: ")
print(df.describe())

print(' ')
print("Finding out the Correlation between the features: ")
corr = df.corr()
print(corr)
print(corr.shape)

print("Plotting the heatmap of correlation between the features: ")
plt.figure(figsize = (14,14))
sns.heatmap(corr, annot=True)
print(' ')
print("Checking null values using heatmap: ")
sns.heatmap(df.isnull(), annot = True, cbar = False, cmap = 'viridis')

sns.distplot(df['age'].dropna(),kde=False,color='darkred',bins=40)
plt.show()