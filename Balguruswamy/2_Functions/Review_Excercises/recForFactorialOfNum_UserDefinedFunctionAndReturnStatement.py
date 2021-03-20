#WAP to implement recursion for factorial of a number that demonstrates the user defined function and return statement

def fact(n):
  if n == 1:
    return n
  else:
    return n * fact(n-1)

num = int(input("Enter a number: "))
if num < 0:
  print("Factorial for negative values does not exist...")
elif num == 0:
  print("Factorial is 1")
else:
  print("Factorial of ",num,"is",fact(num))