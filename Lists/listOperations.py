thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]

print("thislist: {}".format(thislist))
print("tropical: {}".format(tropical))

print(' ')

listMethods = ['Extend', 'Insert', 'Remove', 'Pop', 'Delete', 'Append', 'Clear']
print("List Methods: ")
for i in listMethods:
  print(i)

print(' ')
print("Extend:")
thislist.extend(tropical)
print(thislist)

print(' ')
print("Insert:")
thislist.insert(4, "Nagpur")
print(thislist)

print(' ')
print("Remove:")
thislist.remove("Nagpur")
print(thislist)

print(' ')
print("Pop:")
thislist.pop(1)
print(thislist)

print(' ')
print("Delete:")
del thislist[4]
print(thislist)

print(' ')
print("Append: ")
thislist.append(tropical)
print(thislist)

print(' ')
print("Clear List: ")
thislist.clear()
print(thislist)
print(' ')

thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]

print("thislist: {}".format(thislist))
print("tropical: {}".format(tropical))

print("Extend:")
thislist.extend(tropical)
print(thislist)

print(' ')
print("Looping through list: {}".format("FOR LOOP"))
for i in thislist:
  print(i)

print(' ')
print("Using length of the list: {}".format("FOR LOOP"))
for i in range(len(thislist)):
  print(thislist[i])

print(" ")

print("Using while loop: {}".format("WHILE LOOP"))
i = 0
while i < len(thislist):
  print(thislist[i])
  i = i + 1

print(' ')

print("List comprehension: ")

newlist = []
print("Check whether an element contains letter a or not : ")

for i in thislist:
  if 'a' in i:
    newlist.append(i)

print("Elements of thislist with letter a: ")
print(newlist)
print(' ')

print("Using single line format: ")
newlist = [i for i in thislist if 'a' in i]
print(newlist)
print(' ')

myNewList = ["orange", "mango", "kiwi", "pineapple", "banana"]
print("My new List: {}".format(myNewList))
print("Sorting list: {}".format("Ascending order (By default)"))
myNewList.sort()
print(myNewList)
print(' ')

print("Sorting list: {}".format("Descending order"))
myNewList.sort(reverse=True)
print(myNewList)
print(' ')

print('Case Sensitive Sorting: ')
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort()
print(thislist)
print(' ')

print("Case Insensitive Sorting: ")
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort(key=str.lower)
print(thislist)
print(' ')

print("Sorting the list irrespective of the aplhabet: ")
thislist.reverse()
print(thislist)
print(' ')

print("Copying of list: ")
list2 = thislist.copy()
print(list2)
print(' ')

mylist = list(list2)
print(mylist)
print(' ')

print('List can be multiplied with a scalar: ')
fruits = ['apple', 'banana', 'cherry']
print(fruits * 2)



