import numpy as np
import pandas as pd
from sklearn import datasets
import matplotlib.pyplot as plt

iris = datasets.load_iris()
iris = pd.DataFrame(iris.data, columns = iris.feature_names)
print(iris)
print(iris.head())
print("Shape of the iris data set : ", iris.shape)
print(" ")
print("The list of null elements in the data set: ")
print(iris.isnull().sum())
print(' ')
print("Sum of all the null values: {}".format(iris.isnull().sum().sum()))