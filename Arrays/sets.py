#A set is a collection which is unordered and unindexed. In Python sets are written with 
#curly brackets.
thisSet = {"apple", "banana", "cherry"}
print(thisSet)

print(" ")
print("Looping through sets:")
for x in thisSet:
  print(x)

print(" ")
#if banana is present in the set
print("Whether an element is present in the set or not :")
print("Banana is present in the set: ")
print("banana" in thisSet) # prints True
print(" ")
print("Watermelon is not present in the set: ")
print("watermelon" in thisSet) # prints False

#Adding items to the set
print(" ")
thisSet.add("Watermelon") # Watermelon added to the set 
print(thisSet)