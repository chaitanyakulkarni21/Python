list1 = [1,2,3,4]
list2 = ['a','b','c','d']
print("Before Joining: ")
print("List1: ",list1)
print("List2: ",list2)
print("List Joining: ")
list3 = list1 + list2
print("After Joining list3 becomes : ",list3)

for i in list1:
  list2.append(i)
print("Using For loop: {}".format(list2))

print("Extend method")
list1.extend(list2)
print(list1)