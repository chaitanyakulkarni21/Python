#It is also possible to use tuple constructor tuple() to make a tuple

thisTuple = tuple(("apple","banana","cherry"))  #Note: tuple constructor uses double round-brackets
print("Constructed Tuple is : ",thisTuple)

print(" ")
#single tuple
print("Tuple type: ")
tuple1 = ("apple")
print(type(tuple1)) #Type is string

tuple2 = ("apple",)
print(type(tuple2)) #Type is tuple. Tuple element always ends with a comma  

#Joining of two tuples
print(" ")
print("Joining of two tuples:")
thisTuple1 = ("Tokyo","Berlin","Germany")
thisTuple2 = (1,2,3)
thisTuple3 = thisTuple1 + thisTuple2
print("Tuple 1 : ",thisTuple1)
print("Tuple 2 : ",thisTuple2)
print("Tuple 3 : ",thisTuple3)