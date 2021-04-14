import pandas as pd
import numpy as np

dict = {}
df = pd.DataFrame()

len = int(input("Enter length of dictionary: "))
print(' ')
for i in range(1, len+1):
  key = input("Enter key : ")
  value = input("Enter value for key {} : ".format(key))
  print(' ')
  dict[key] = value
print(' ')
print("Dictionary: ")
print(dict)

df = pd.DataFrame(dict.items(), columns = ['A','B'])
print(' ')
print(df)