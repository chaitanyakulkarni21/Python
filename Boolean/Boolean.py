#When we compare two numbers, the expression is evaluated and the Python 
# returns a Boolean answer TRUE or FALSE 
print("Boolean expressions :")
print(10 > 9) #returns TRUE
print(10 == 9) #returns FALSE
print(10 < 9) #returns FALSE

print(" ")
#Python returns TRUE or FALSE in an if statement 
print("Use of Boolean in if-else:")
a = 5
b = 60
if a > b:
    print("a is greater than b")
else:
    print("b is greater than a")

print(" ")

#The bool() function evaluates any value as TRUE / FALSE 

print("Bool Function: ")
print(bool("Hello")) #Returns TRUE
print(bool(25))     #Returns TRUE
print(bool(20<9))   #Returns FALSE 

print(" ")
print("Evaluate two variables : ")
x = 17
y = 23
z = 0
print(bool(x))  #TRUE
print(bool(y))  #TRUE
print(bool(z))  #FALSE

print(" ")

print("Empty String : ")
x = "" #Empty String
print(bool(x))
print(" ")

#The following will return false
print("Empty strings Statements: ")
print(bool(False))
print(bool(None))
print(bool(0))
print(bool(""))
print(bool(()))
print(bool([]))
print(bool({}))




