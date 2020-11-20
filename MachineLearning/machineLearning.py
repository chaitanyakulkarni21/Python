#NUMPY MODULE
print(" ")

#Creating an array using the Numpy module 
print("Creating an array using the numpy module :")
import numpy                    #NumPy module is imported 
arr = numpy.array([1,2,3,4,5])  #Creates an array using the module numpy
print(arr)                      #Prints the created array 
print(type(arr))                #Prints the class of the array 
print(" ")


#Calculating Mean and Median using the NumPy module
import numpy
speed = [23,56,23,45,23,23,78,15,66,23,2,89]
avg = numpy.mean(speed)           #Calculates the mean of the numbers 
print("The mean of the given numbers is : ",avg)
print(" ")
avg = numpy.median(speed)         #Calculates the median (middle value)
print("The median of the given numbers is : ",avg)
print(" ")

#Calculating the mode of the given numbers 
from scipy import stats                   #mode method is imported from SciPy library
avg = [23,56,23,45,23,23,78,15,66,23,2,89]
x = stats.mode(avg)
print("The mode of the given numbers is : ", x) #The mode() method returns the ModeResult(Modenumber and mode count)
print(" ")


#Calculating Standard Deviation
import numpy
speed = [23,56,23,45,23,23,78,15,66,23,2,89]
avg = numpy.std(speed)
print("The Standard Deviation is : ",avg)
print(" ")

#Calculating Variance using the Numpy method
import numpy
avg = [45,67,89,12,34,56,78,90]
x = numpy.var(avg)
print("The Variance of the entered array is :",x)
print(" ")

#Calculating Percentile using the Numpy method 
import numpy
ages = [5,31,43,48,50,41,7,11,15,39,80,82,32,2,8,6,25,36,27,61,31]
print(ages)
x = numpy.percentile(ages,75)
print("Percentile : ",x)
print(" ")

#Data Distribution
#Generating random sets of numbers using the Numpy method 
import numpy
x = numpy.random.uniform(0,5,10)
print(x)
print(" ")

#Histogram
#Draw a histogram
import numpy
import matplotlib.pylot as plt 
x = numpy.random.uniform(0.0,5.0,250)
plt.hist(x,5)
plt.show()
print(" ")