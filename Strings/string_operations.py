# Printing a string
x = "Hello, World!"
print(x)
print(" ")

# Length of a String
print("The length of the string is: ",len(x))
print(" ")

#Range of characters in strings (Slicing)
print("The string characters from index 2 to index 4 are: ",x[2:5]) # index 5 is not included
print("The string characters from index 1 to index 6 are: ",x[1:6]) # index 6 is not included
print("The string characters from index -5 to index -1 are: ",x[-5:-1]) # string counting is from backwards
print("The string characters from index -6 to index -1 are: ",x[-6:-1]) # string counting is from backwards
print(" ")

#String with White Spaces 
y = "   Good Morning!!"
print("Strip method eliminates any whitespaces in the begining... : ")
print(y.strip())
print(" ")

#String in uppercase 
print("String in Upper case is : ",x.upper())
#String in lowercase 
print("String in Lower Case is : ",x.lower())
print(" ")

#Replacing characters in strings
print("Replace H with G and W with M in the String Hello World....")
print(x.replace("H","G"))
print(x.replace("W","M"))
print(" ")

#Split Method 
print("Split method splits the string in to two sub strings:..")
print(x.split())
print(" ")

#Concatenation of Strings
a = "Hello"
b = "World"
print("Before Concatenation:",a,b)
c = a+b
print("After Concatenation",c)  #prints the concatenated string "HelloWorld"
print(" ")

#Checking a phrase in the string
str = "The rain in the Spain stays mainly in the plain"
print(str)
x1 = "ain" in str
print(x1) # returns a boolean value: True or False, True in this case
print(" ")

#String format
age = 26
txt = "My name is Steve. I am {} years old"
print(txt.format(age))
print(" ")

#Multiple arguments in Format method
Qty = 3
ItemNo = 123
Price = 500
myOrder = "I want {} pieces of item {} for {} dollars"
print(myOrder.format(Qty,ItemNo,Price)) #Values are printed in this order
print(" ")