class Student:
  def getInfo(self):
    self.fname = input("Enter First Name: ")
    self.lname = input("Enter Last Name: ")

  def printInfo(self):
    print("First Name: {}".format(self.fname))
    print("Last Name: {}".format(self.lname))

s = Student()
s.getInfo()
print(' ')
s.printInfo()
    