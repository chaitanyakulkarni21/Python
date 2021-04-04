class Arithmetic:
  def __init__(self, num1, num2):
    self.num1 = num1
    self.num2 = num2

  def add(self):
    return(self.num1 + self.num2)

  def mul(self):
    return(self.num1 * self.num2)

  def diff(self):
    return(self.num1 - self.num2)

  def rem(self):
    return(self.num1 / self.num2)
  
  def quo(self):
    return(self.num1 % self.num2)

num1 = int(input("Enter num1: "))
num2 = int(input("Enter num2: "))

ar = Arithmetic(num1, num2)
print(' ')
sum = print("Sum: ",ar.add())
mul = print("Product: ",ar.mul())
diff = print("Difference: ",ar.diff())
rem = print("Remainder: ", ar.rem())
quo = print("Quotient: ", ar.quo())