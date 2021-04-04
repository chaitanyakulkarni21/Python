class Student:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def printInfo(self):
    print("Student Name: ", self.name)
    print("Student Age: ", self.age)


name = input("Enter Student Name: ")
age = int(input("Enter Student Age: "))

s = Student(name, age)
s.printInfo()
