from numpy import mean
from scipy.stats import gmean
from scipy.stats import hmean

# example of calculating the arithmetic mean
# define the dataset
data = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# calculate the mean
result = mean(data)
print('Arithmetic Mean: %.3f' % result)


# example of calculating the geometric mean
# define the dataset
data = [1, 2, 3, 40, 50, 60, 0.7, 0.88, 0.9, 1000]
# calculate the mean
result = gmean(data)
print('Geometric Mean: %.3f' % result)


# example of calculating the harmonic mean
# define the dataset
data = [0.11, 0.22, 0.33, 0.44, 0.55, 0.66, 0.77, 0.88, 0.99]
# calculate the mean
result = hmean(data)
print('Harmonic Mean: %.3f' % result)