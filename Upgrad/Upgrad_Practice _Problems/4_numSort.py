# Q.4 Write a program to accept n numbers from the user and store these numbers into an array and sort the numbers using function

n = int(input("How many numbers you want to add : "))
numbers = []
for i in range(1,n+1):
    numbers.append(int(input("Enter numbers:")))
print("Numbers Before Sorting: ",numbers)
print("Numbers After Sorting: ",sorted(numbers))