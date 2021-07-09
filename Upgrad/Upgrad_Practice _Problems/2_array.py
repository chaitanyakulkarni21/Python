# Q.2 WAP to accept n numbers from the user, store these numbers in an array. Find the max and min numbers

count = int(input("How many numbers you want to enter: "))
num = []
print("Enter",count,"numbers: ")
while count > 0:
	num.append(int(input("Enter num: ")))
	count = count -1 
print("List of numbers: ",num)
print("Max number:",max(num), "Min number: ",min(num))