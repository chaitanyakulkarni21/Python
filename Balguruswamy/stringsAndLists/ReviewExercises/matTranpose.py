#WAP to print the transpose of a given matrix
arr = [[1,2], [3,4], [6,7]]
trans = [[0,0,0], [0,0,0]]
for i in arr :
  for j in trans:
    trans[j][i] = arr[i][j]
print(trans)
