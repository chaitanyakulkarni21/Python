# Q.10 WAP to accept a string and delete all the vowels from the string and display the result 

string = input("Enter a string: ")
vowels = [string.remove() for v in string if v in 'aeiouAEIOU']
print(vowels)