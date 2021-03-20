import numpy as np
arr = np.array([[1,2,3],[4,5,6]]) 
print("Array1:\n",arr)
print(' ')
arr2 = np.array([[1,2,3],[4,5,6],[7,8,9]])
print("Array2:\n",arr2)

print('Arrays of Ones and Zeros:\n')
ones = np.ones((3,3))
print('Array of Ones: \n',ones)
print(' ')

zeros = np.zeros((3,3))
print("Array of Zeros:\n", zeros)
print(' ')

print("Linspace: ")
print("Linspace returns evenly spaced array of values")
linspace_arr = np.linspace(0,40,20)
print(linspace_arr)
print(' ')

print('eye: prints the unity matrix')
print(np.eye(4))
print(' ')
print(np.eye(9))
print(' ')

print('Random.randn:')
arr3 = np.random.randn(3,4)
print(arr3)
print(' ')

print('Arange:')
arr4 = np.arange(25)
print(arr4)
print(' ')
ranarr = np.random.randint(0,50,10) # Generates and array of 10 random values from 0 to 50
print(ranarr)
print(' ')
print('Reshape converts the 1-d array into a 2-d array: ')
print(ranarr.reshape(2,5)) # 2*5 = 10 => no. of elements in the actual array
print(' ')

print('Min Max Argmin and Argmax : ')
ranarr2 = np.random.randint(0,30,10)
print(ranarr2)
print("Max value: ", ranarr2.max())
print("Index of Max value: ", ranarr2.argmax())
print("Min value: ", ranarr2.min())
print("Index of Min value: ", ranarr2.argmin())
print(' ')