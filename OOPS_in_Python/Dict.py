class Dictionary:
  dict = {}
  def addItems(self):
    len = int(input("Enter length of Dictionary: "))
    for i in range(1,len+1):
      key = input("Enter key : ")
      value = input("Enter value for the key {}: ".format(key))
      print(' ')
      self.dict[key] = i
      self.dict[key] = value
    print("Dictionary : ", self.dict)

class List:
  list = []
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
d = Dictionary()
d.addItems()
print(' ')
l = List()
l.addItems()
