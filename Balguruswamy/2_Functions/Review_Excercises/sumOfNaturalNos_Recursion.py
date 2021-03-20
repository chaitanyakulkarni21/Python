#WAP to find the sum of several natural numbers using recursion

def sum_rec(n):
  if n<= 1:
    return n
  else:
    return n + sum_rec(n-1)
print(sum_rec(int(input("How many natural numbers? : "))))