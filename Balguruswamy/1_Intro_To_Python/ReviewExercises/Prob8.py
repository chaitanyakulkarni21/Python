#WAP to display the Fibonacci series for n terms 
n = int(input("Enter the value for n (where n > 2)?: "))
x1 = 0
x2 = 1
count = 2
if n <= 0:
  print("Please enter a positive integer")
elif n == 1:
  print("Fibonacci Sequence is : ")
  print(x1)
else:
  print("Fibonacci Sequence is : ")
  print(x1 , x2)
  while count < n:
    xth = x1 + x2
    print(xth)
    x1 = x2
    x2 = xth
    count += 1