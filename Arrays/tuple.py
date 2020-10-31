# A tuple is a collection which is ordered and UNCHANGABLE. Written within round brackets

thisTuple = ("apple", "banana", "mango", "cherry", "papaya", "watermelon")
print("The entered Tuple is : ",thisTuple)

print("Printing individual items of the Tuple: ")
print(thisTuple[0])
print(thisTuple[1])
print(thisTuple[2])
print(thisTuple[3])
print(thisTuple[4])
print(thisTuple[5])

# thisTuple[2] = "chaitanya"  # Tuple is unchangeable
# print(thisTuple)

#printing the tuple from last 
#Negative indexing prints from last 
print(" ")
print("printing the tuple from last:")
print(thisTuple[-1])
print(thisTuple[-2])
print(thisTuple[-3])
print(thisTuple[-4])
print(thisTuple[-5])
print(thisTuple[-6])

#Range 
print(" ")
print("Range of tuple : ")
print(thisTuple[:5])  # from thisTuple[0](included) to thisTuple[5](not included)
print(thisTuple[1:])  # from thisTuple[1](included) to thisTuple[5](included)
print(thisTuple[1:5]) # from thisTuple[1](included) to thisTuple[5](not included)

#Removing an item from the list 
print(" ")
#thisTuple.remove("banana")  #Items in a tuple cannot be removed. This will raise an error 

#Length of the tuple
print("The length of this tuple is : ",len(thisTuple))