import pandas as pd
import numpy as np 

class Dictionary:
  dict = {}
  #df = pd.DataFrame()
  def addItems(self):
    len = int(input("Enter length of Dictionary: "))
    for i in range(1,len+1):
      key = input("Enter key : ")
      value = input("Enter value for the key {}: ".format(key))
      print(' ')
      self.dict[key] = i
      self.dict[key] = value
    print(' ')
    print("Dictionary: ", self.dict)
    df = pd.DataFrame(self.dict.items())
    print("Dictionary to Data Frame: ")
    print(df)

class List:
  list = []
  series = pd.Series()
  def addItems(self):
    len = int(input("Enter the length of List: "))
    for i in range(1, len+1):
      if i == 1:
        self.list.append(input("Enter {}st list item: ".format(i)))
      elif i == 2:
        self.list.append(input("Enter {}nd list item: ".format(i)))
      else:
        self.list.append(input("Enter {}th list item: ".format(i)))
    print(' ')
    print("List: ", self.list)
    series = pd.Series((i[0] for i in self.list))
    print("List to Series: ")
    print(series)

d = Dictionary()
d.addItems()
print(' ')
l = List()
l.addItems()

