# Q.1 WAP to accept a 4 digit number and count zer, odd and even digits from the entered number

num = input("Enter a 4 digit number: ")
evenList = []
evenCount = 0
oddCount = 0
zeroCount = 0
oddList = []
for i in num:
    if int(i)%2 == 0:
        evenList.append(int(i))
        evenCount = evenCount + 1
    else:
        oddList.append(int(i))
        oddCount = oddCount + 1
print("Even Digits: ",evenList, "Count: ",evenCount)
print("Odd Digits :",oddList, "Count: ",oddCount)