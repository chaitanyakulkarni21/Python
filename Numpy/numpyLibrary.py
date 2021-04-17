import numpy as np


print("Version of numpy : ")
print(np.__version__)
print(' ')

arr0 = np.array(34)
print("Array 0D: {}".format(arr0))
print("Dimension: ", arr0.ndim)
print(' ')

arr1 = np.array([1,2,3,4,5,6,7,8,9])
print("Array 1D: {}".format(arr1))
print("Dimension: ", arr1.ndim)
print(' ')

arr2 = np.array([[1,2,3],[4,5,6],[7,8,9]])
print("Array 2D:")
print(arr2)
print("Dimension: ", arr2.ndim)
print(' ')

arr3 = np.array([[[1,2,3], [4,5,6], [7,8,9]]])
print("Array 3d: ")
print(arr3)
print("Dimension: ", arr3.ndim)
print(" ")

print("Printing the number of dimensions: ")
print("Dimension: ", arr0.ndim)
print("Dimension: ",arr1.ndim)
print("Dimension: ",arr2.ndim)
print("Dimension: ",arr3.ndim)
print(' ')

print("Creating a 5 dim array: ")
arr5 = np.array([1,2,3,4,5], ndmin = 5)
print("Array 5d: ")
print(arr5)
print("Dimension: ", arr5.ndim)
print(' ')

print("Creating a 4 dim array: ")
arr4 = np.array([4,5,6,7,8], ndmin = 4)
print("Array 4d: {}".format(arr4))
print("Dimension: {}".format(arr4.ndim))
print(' ')

print("Array Indexing in 1d array: ")
print("4th index of array 1: ",arr1[4])
print(' ')

print("Array indexing in 2d Array: ")
print('5th element on 2nd dim: ', arr2[1, 2])
print(' ')

print("Array indexing in 3d array: ")
print("5th element in 3d array: ", arr3[0, 1, 2])
print(' ')

print("Negative Indexing: ")
print("Last element of 2d array: ", arr2[2,-1])
