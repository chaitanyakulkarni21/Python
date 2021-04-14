# Program to find the sum of squares of first n natural numbers 

def sumOfSq(n):
  s = 0
  for i in range(1, n+1):
    s = s + i**2
  return s

n = int(input("Enter the last number in the series: "))
sum = print("The Sum of squares of the natural numebers is : ",sumOfSq(n))