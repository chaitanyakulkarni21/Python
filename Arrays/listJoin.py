#Joining two list
print("Using simple method : ")
list1 = ['a','b','c','d']
list2 = [1,2,3,4]
print("List 1 is : ",list1)
print("List 2 is : ",list2)
list3 = list1 + list2
print("List 3 is : ")
print(list3)

# Another way to join two lists is, to append all the items from one list to another one by one

print(" ")
print("Using append method: ")
list1 = ['a','b','c','d']
list2 = [1,2,3,4]
print("List 1 is : ",list1)
print("List 2 is : ",list2)
print(" ")
for x in list2:
  list1.append(x)
print("List1 after appending is: ",list1)
print(list1)

#Or you can use the extend() method, which purpose is to add elements from one list to another list
list1 = ['a','b','c','d']
list2 = [1,2,3,4]
print("List 1 is : ",list1)
print("List 2 is : ",list2)
print(" ")
print("Using extend() method:")
list1.extend(list2)
print("List1 after extending is: ",list1)