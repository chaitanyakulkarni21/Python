#Copying a List

#Method 1: copy() method
list1 = ["apple", "banana", "cherry"]
print("List 1 is : ")
print(list1)
list2 = list1.copy()
print("After copying lsit 1 to list 2, list 2 becomes : ")
print(list2)

#Method 2: Built-in list() method
print(" ")
thisList = ["apple", "banana", "cherry"]
print("thisList  is: ")
print(thisList)
myList = list(thisList)
print("myList  after copying: ")
print(myList)

