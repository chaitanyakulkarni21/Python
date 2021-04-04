class Person:
  def __init__(self, personName = None):
    self.personName = personName
  
  def printName(self):
    if self.personName != None:
      print("Hello " + self.personName)
    else:
      print("Hello")

name = input("Enter your name: ")
p = Person(name)
p.printName()