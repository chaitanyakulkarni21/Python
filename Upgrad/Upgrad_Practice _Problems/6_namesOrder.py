#Q.6 WAP to accept 5 names from the user and store in an array. Sort the names in alphabetical order.
names = []
n = int(input("How many names you want to add ? :"))
print("Add",n,"names: ")
for i in range(1,n+1):
    names.append(input("Enter name :"))
print("Before sorting: ")
print(n,"names in the array are : ",names)
print("After sorting: ",sorted(names))