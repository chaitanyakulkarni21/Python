myTuple1 = (4,6,3,4,5,7,8,9,2)
print("Tuple: ",myTuple1)

print("Accessing tuple elements")
for i in myTuple1:
  print(i)

print("Element at index 6 : ",myTuple1[6])
print("Length of Tuple: ", len(myTuple1))

myTuple2 = (4,3,2,5,6,7,8)
print("Tuple 1: ",myTuple1)
print("Tuple2: ", myTuple2)
myTuple3 = myTuple1 + myTuple2
print("Tuple 1 + Tuple 2: ",myTuple3)

print(' ')

print("Tuple Slicing")
print(myTuple1[4:7])
print(myTuple1[1:6])
print(myTuple1[6:])
print(myTuple1[:7])

print(' ')
print("Negative Indexing")

print(myTuple1[-1:])
print(myTuple1[-4:-1])
print(myTuple1[-5:-3])
print(myTuple1[-8:])
print(myTuple1[-7:-1])

print("Adding elements in the tuple: ")
print(myTuple1)
print("Tuple converted into List: ")
y = list(myTuple1)
print(y)
y.append("Orange")
print("After appending an element, the list is converted back into Tuple: ")
myTuple1 = tuple(y)
print(myTuple1)

print(' ')
print("Removing an item from tuple")
list2 = list(myTuple2)
list2.append("New element")
myTuple2 = tuple(list2)
print("New element added: ")
print(myTuple2)

list2 = list(myTuple2)
list2.remove("New element")
myTuple2 = tuple(list2)
print("New element removed")
print(myTuple2)
