#WAP to find the duplicate characters in the given list 

str = 'java'
single = []
duplicate = []
count = 0
for i in 'java':
  if str.count(i) > 1:
    duplicate.append(i)
  else:
    single.append(i)

print("Complete List: ", str)
print("List of single characters : ", single)
print("List of duplicate characters: ",duplicate)