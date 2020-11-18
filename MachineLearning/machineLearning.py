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
from scipy import stats 
avg = [23,56,23,45,23,23,78,15,66,23,2,89]
x = stats.mode(avg)
print("The mode of the given numbers is : ", avg)