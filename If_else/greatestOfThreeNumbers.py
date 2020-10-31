#Greatest of Three Numbers 

x = input("Enter num1 : ")
y = input("Enter num2 : ")
z = input("Enter num3 : ")

if (x > y) and (x > z):
   largest = x
elif (y > x) and (y > z):
   largest = y
else:
   largest = z
 
print("The largest number is",largest)