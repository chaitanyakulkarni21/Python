class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age
  
  def printData(self):
    print("Name : ", self.name)
    print("Age: ", self.age)

p1 = Person("John", 36)
p1.printData()
