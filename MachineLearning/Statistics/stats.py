import numpy as np
from scipy import stats


speed = [86,87,88,86,87,85,86]
print("Speed: ",speed)
print("Mean: ",np.mean(speed))
print("Mode: ",stats.mode(speed))
print("Median: ",np.median(speed))
print("Standard Deviation: ",np.std(speed))
print("Variance: ",np.var(speed))

speed2 = [32,111,138,28,59,77,97]
print(" ")
print("Speed 2: ", speed2)
print("Mean of speed 2 = ",np.mean(speed2))
print("Mode: ",stats.mode(speed2))
print("Median: ",np.median(speed2))
print("Standard Deviation: ",np.std(speed2))
print("Variance = ",np.var(speed2))
print(' ')
#Percentile

ages = [5,31,43,48,50,41,7,11,15,39,80,82,32,2,8,6,25,36,27,61,31]
print("Ages: ",ages)
print("Percentile: ",np.percentile(ages,90))
print("Percentile: ",np.percentile(ages,75))
