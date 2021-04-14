
thisSet = {'a','b','c','d','e'}
print("Set: ", thisSet)

print("Looping through Set: ")
for i in thisSet:
  print(i)

print(" ")

print("Search an element in the set ")
x = input("Enter the element you want to search in the set: ")

if x in thisSet:
  print("Yes, the element {} is present in the set".format(x))
else:
  print("No, the element {} is not present in the set".format(x))

print("Adding elements in the set")
thisSet.add("Nagpur")
print(thisSet)

print(' ')
add = input("Enter the element you want to add in the set: ")
thisSet.add(add)
print(add," element added")
print(thisSet)

remove = input("Enter the element you want to remove from the set: ")
thisSet.remove(remove)
print(remove," element removed")
print(thisSet)