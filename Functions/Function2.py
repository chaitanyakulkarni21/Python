def sum(num1, num2):
  return num1 + num2
 
num1 = int(input("Enter num 1: "))
num2 = int(input("Enter num 2: "))
s = sum(num1, num2)
print('Sum: ',s)

def greatestOfTwo(num1, num2):
  if num1 > num2:
    print(num1,"is greater")
  else:
    print(num2,"is greater")

greatestOfTwo(num1, num2)