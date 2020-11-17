def myFunction():
  print("Hello world from a function...")

myFunction()
print(" ")

#Passing arguments to a function

def Function1(fname):
  print(fname + " Kulkarni")
fname = "Chaitanya"
Function1(fname)

print(" ")

#Passing Multilple arguments to a function

Fname = "Devashish"
Lname = "Pande"

def MultilpleArg(Fname, Lname):
  print(Fname + Lname)

MultilpleArg(Fname, Lname)

#Arithmetic Operations using Functions 
def ArithmeticOperations(x,y):
  print(x + y)
  print(x - y)
  print(x * y)
  print(x / y)
  print(x % y)
ArithmeticOperations(4,5)