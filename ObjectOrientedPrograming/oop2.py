class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myFunc(self):
    print("Hello, my name is {} and age is {}".format(self.name,self.age))

p = Person('Chaitanya', 26)
p.myFunc()
print(' ')

class ArithmeticOperations:
  def __init__(self, num1, num2):
    self.num1 = num1
    self.num2 = num2

  def printNum(self):
    print("Two numbers are :",self.num1, self.num2)

class Sum(ArithmeticOperations):
  def __init__(self, num1, num2):
    ArithmeticOperations.__init__(self, num1, num2)

  def calSum(self):
    self.num3 = self.num1 + self.num2
    print("Sum = ",self.num3)

class Difference(ArithmeticOperations):
  def __init__(self, num1, num2):
    ArithmeticOperations.__init__(self, num1, num2)

  def calDiff(self):
    self.num3 = self.num1 - self.num2
    print("Difference = ",self.num3)

class Product(ArithmeticOperations):
  def __init__(self, num1, num2):
    ArithmeticOperations.__init__(self, num1, num2)

  def calProd(self):
    self.num3 = self.num1 * self.num2
    print("Product = ",self.num3)
x = int(input("Enter num 1: "))
y = int(input("Ente num 2: "))

sum = Sum(x,y)
sum.printNum()
sum.calSum()

prod = Product(x,y)
prod.calProd()

diff = Difference(x,y)
diff.calDiff()
print(' ')