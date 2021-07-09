# 1. Print the following pattern 
# 1,2,3,4,5
for i in range(1,6):
    print(i, end = " ")
print(' ')
# 2. Print the following pattern 
# 1 1 1 1 1
for i in range(1,6):
    print(1,end = " ")
print(' ')
# 3. Print the following pattern
# 5 4 3 2 1
for i in range(5,0,-1):
    print(i, end = ' ')
print(' ')
# 4. Print the following pattern
'''
1
1 2
1 2 3
1 2 3 4 
1 2 3 4 5
'''
for x in range(1,6):
    for y in range(1,x+1):
        print(y, end = ' ')
    print()
print(' ')
# 5. Print the following pattern
'''
5 4 3 2 1
5 4 3 2
5 4 3
5 4
5
'''
for x in range(1,6):
    for y in range(5,x-1,-1):
        print(y, end = " ")
    print()
print(' ')