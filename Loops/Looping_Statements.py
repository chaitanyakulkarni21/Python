print("Printing 0 to 10: ")
count = 0
while(count < 11):
    print("The value of count is : ", count)
    count = count + 1
print("Other Statements...")
print(' ')

print("Printing 10 to 0: ")
count = 10
while count >= 0:
    print("The value of count : ", count)
    count = count - 1
print("Other Statements...")
print(' ')

print("Table of 2:")
n = 2
i = 1
while i <= 10:
  p = n * i
  print(p)
  i = i + 1 
print(' ')

n = int(input("Enter a number: "))
print("Table of ", n)
i = 1
while i <= 10:
  p = n * i
  print(p)
  i = i + 1
print(' ')

for i in range(5):
    print('Current index is: ', i)
print(' ')

for i in range(1,5,1): #range(start,stop,steps)
    print('Current index is: ', i)
print(' ')

for i in range(3,10,2):
    print('Current index is: ',i)
print(' ')

for i in range(3,10):
    print('Current index is: ',i)
print(' ')

for i in range(10,1,-1):
    print('Current index is: ',i)
print(' ')

for i in range(10,1,-2):
    print('Current index is: ',i)
print(' ')

for i in range(10,0,-1):
    print('Current index is: ',i)
print(' ')

#Printing table using for 
print("Table of 2:")
for i in range(1,11):
    p = 2 * i
    print(p)
print(' ')

n = int(input("Enter a number: "))
print("Table of ",n)
for i in range(1,11):
    p = n * i
    print(p)
print(' ')
