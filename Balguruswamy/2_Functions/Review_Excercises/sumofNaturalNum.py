def sum_nat(n):
  s = 0
  for i in range(1, n+1):
    s = s + i
  print("Sum of",n,"Natural numbers: ", s)

x = int(input("How many natural numbers ? : "))
sum_nat(x)