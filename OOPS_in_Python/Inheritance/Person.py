#Inheritance in Python

class Person:
  def __init__(self, fname, lname):
    self.fname = fname
    self.lname = lname

class Student(Person):
  def __init__(self, fname, lname):
    Person.__init__(self, fname, lname)
    self.graduationYear = 2014

  def studentData(self):
    print("Student Name: {}  {}".format(self.fname, self.lname))
    print("Graduation Year: {}".format(self.graduationYear))

firstName = input("Enter first name: ")
lastName = input("Enter last name: ")
s = Student(firstName, lastName)
s.studentData()
