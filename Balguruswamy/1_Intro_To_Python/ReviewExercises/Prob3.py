#WAP to swap two numbers
x = int(input("Enter num1: "))
y = int(input("Enter num2: "))
print('Before Swapping: x = {} and y = {}'.format(x,y))
t = x
x = y
y = t
print("After swapping: x = {} and y = {}".format(x,y))