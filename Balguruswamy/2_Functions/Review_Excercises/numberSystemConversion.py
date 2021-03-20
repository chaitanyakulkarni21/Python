#WAP to convert a decimal number into binary, octal, hexadecimal equivalents

def Conversion(n):
  print("The binary of ", n, "is: ", bin(n))
  print("The octal of ", n, "is: ", oct(n))
  print("The hexadecimal of ", n, "is: ", hex(n))

x = int(input("Enter a number: "))
Conversion(x)