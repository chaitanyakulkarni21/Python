#Break
print("Break Statement 1...")
print(' ')

for letter in 'Python':
  if letter == 'h':
    break
  print("Current letter is : ",letter)
print('Out of loop...')
print(' ')

print("Break Statement 2...")
print(' ')

var = 10
while var > 0:
  if var == 5:
    break
  print("Current value of var is : ",var)
  var = var - 1
print("Out of Loop...")
print(' ')

#Continue
print("Continue Statement 1...")
print(' ')

for letter in "Python":
  if letter == 'h':
    continue
  print("Current value is : ", letter)
print('Out of loop...')
print(' ')

print('Continue Statement 2...')
print(' ')

var = 10
while var > 0:
  var = var - 1
  if var == 5:
    continue
  print('Current value of var is : ',var)
print('Out of loop...')
print(' ')

