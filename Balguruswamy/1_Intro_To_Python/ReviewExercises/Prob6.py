#WAP to check the largest of three numbers
x = int(input("Enter num1: "))
y = int(input("Enter num2: "))
z = int(input("Enter num3: "))

if x > y:
  if x > z:
    print(x, "is large")
  else:
    print(z, "is large")
elif y > z:
    print(y,"is large")
else:
    print(z,"is large")