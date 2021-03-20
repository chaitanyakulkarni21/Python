print(' ')
class SchoolMember:
  def __init__(self,name,age):
    self.name = name
    self.age = age
    print("Intialised School Member:",self.name)

class Teacher(SchoolMember):
  def __init__(self,name,age,salary):
    SchoolMember.__init__(self,name,age)
    self.salary = salary
    print("Initialised Teacher: ",self.name)
    print("Salary:",self.salary)

class Student(SchoolMember):
  def __init__(self,name,age,marks):
    SchoolMember.__init__(self,name,age)
    self.marks = marks
    print("Intialised Student : ",self.name)
    print("Marks:",self.marks)

t = Teacher("Mr Shree", 40, 30000)
print(' ')
s = Student("Chaitanya",26,100)
print(' ')