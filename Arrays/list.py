# List is a collection which is ordered and changeble. Allows multiple members 
thisList = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print("The entered list is : ")
print(thisList)

print("Printing the list using positive indexing : ")
print(thisList[0])
print(thisList[1])
print(thisList[2])
print(thisList[3])
print(thisList[4])
print(thisList[5])
print(thisList[6])
print(" ")

print("Printing the list using negative indexing : ")
#Negative indexing of list
print(thisList[-1]) # last item in the list
print(thisList[-2]) # second last item in the list
print(thisList[-3]) # third last item in the list 

#Range of indexes
print(" ")
print("Range :")
print(thisList[2:5]) # prints thisList[2], thisList[3], thisList[4]
print("The search will start at index 2 (included) and end at index 5 (not included)")
print("Hence the output...")

print(" ")
print("Starting the range from 1st value : ")
print(thisList[:4]) # prints thisList[0],thisList[1],thisList[2],thisList[3]
print("By leaving the end value, the range will go to the end of the list ")
print("Hence the output...")

print(" ")
print(thisList[2:])
print("This will print from thisList[2] upto the end of the list")

print(" ")
print("Range of Negative Indexing: ")
print(thisList[-5:-1])

#Changing the item in the list..
print(" ")
thisList[2] = "chaitanya"
print(thisList)
print(thisList[1:4])

#Check if item exist in the list
print(" ")
print("Check if chaitanya exist in the list :")
if "chaitanya" in thisList :
    print("Yes, chaitanya is in this list...")

if "watermelon" in thisList:
  print("No, watermelon does not exist in the list")

#Length of the list..
print(" ")
print("The length of the list is : ",len(thisList))
#print(len(thisList))

#Append an item in the list 
print(" ")
thisList.append("Watermelon") #Appends watermelon at the end of the list
print(thisList)

#Inserting an item to the given index
print(" ")
thisList.insert(2, "coconut")
print(thisList)

#Removing an item from the list 
print(" ")
thisList.remove("banana")
print(thisList)
thisList.append("orange")
print(thisList)
thisList.remove("orange")
print(thisList)

#pop: removes the item of specific index
print(" ")
thisList.pop(3) #removes thisList[3]
print(thisList)

#del: removes the item of specific index
print(" ")
del thisList[6] #removes thisList[3]
print(thisList)

#del keyword can also delete the list completely 
del thisList  # Deletes the list completely

print(" ")
myList = ["A", "B","C","D","E","F"]
print("myList is : ")
print(myList)

#clear() method empties the list
# myList.clear()
# print(myList)
