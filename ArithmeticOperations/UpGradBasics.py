# To find the data type of a variable

integerNum = 45
floatNum = 34.98
string = 'Mike'
boolean = True

print("The type of integerNum is: ", type(integerNum))
print("The type of floatNum is: ", type(floatNum))
print("The type of stirng is: ", type(string))
print("The type of boolean is: ", type(boolean))
print(' ')

print("Typecasting a variable : ")
print(bool(integerNum))
print(float(integerNum))
print(str(integerNum))
print(' ')

print("Data Type of a Typecasted variable : ")
print(type(bool(integerNum)))
print(type(float(integerNum)))
print(type(str(integerNum)))
print(' ')

print("Arithmetic Operations: ")
a = 6
b = 7
print("Addition: ",a+b)
print("Subtraction: ",a-b)
print("Multiplication: ",a*b)
print("Division: ",a/b)
print("Floor Division: ",a//b)