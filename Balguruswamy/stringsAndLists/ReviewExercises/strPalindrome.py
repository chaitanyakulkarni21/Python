#WAP to check whether a string is palindrome or not 

str = input("Enter a string: ")
print(str[:])
print(str[::-1])
if str[:] == str[::-1]:
  print("The given string is a palindrome...")
else:
  print("The given string is not a palindrome...")