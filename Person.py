class Person:
    def setInfo(self, name, age):
        self.name = name
        self.age = age

    def printInfo(self):
        print("Name:", self.name, "Age:", self.age, end=" ")


class Principal(Person):
    def setDesgination(self, desgination):
        self.designation = desgination

    def printDesignation(self):
        print("Designation: ", self.designation)


class Student(Person):
    def printBranch(self, branch):
        self.branch = branch
        print("Branch: ", self.branch)


p1 = Principal()
print("Enter Faculty Info: ")
p1.name = input("Enter name: ")
p1.age = int(input("Enter age: "))
p1.designation = input("Enter Designation: ")
print(' ')

s = Student()
print("Enter Student Info: ")
s.name = input("Enter name: ")
s.age = int(input("Enter age: "))
stream = input("Enter student stream: ")
print(' ')

print("You have entered the following info: ")
print("Principal Info: ")
p1.printInfo()
p1.setDesgination(p1.designation)
p1.printDesignation()
print(' ')

print("Student Info: ")
s.setInfo(s.name, s.age)
s.printInfo()
s.printBranch(stream)
