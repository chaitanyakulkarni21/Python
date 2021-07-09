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
print(" ")

print("Copying and Viewing of Arrays ")
print("Copying of Arrays: ")
x = arr1.copy()
print("Original Array: ", arr1)
print("Copied array: ",x)
x[3] = 999
print("Original Array: ", arr1)
print("Updated copied array: ", x)
print("Changes made in the copied array does not affect the original array")
print(' ')

print("Viewing of Arrays: ")
y = arr1.view()
print("Original array: ", arr1)
print("Viewed array: ", y)
print(' ')
y[4]=19999
print("Original array: ", arr1)
print("Viewed array: ", y)
print("Changes made in the viewed array are reflected into the Original Array")
print(' ')

print("Check if the array owns the data: ")
print("Copied: ", x.base)
print("Viewed: ",y.base)