#WAP to print the fibonacci series using recursion

def fibo_rec(x):
  if x <= 1:
    return x
  else:
    return(fibo_rec(x-1) + fibo_rec(x-2))

num_terms = int(input("Enter the number of terms : "))
for i in range(num_terms):
  print(fibo_rec(i))