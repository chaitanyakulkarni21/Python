#WAP to check whether an year is leap year or not 
yr = int(input("Enter any year: "))
if yr % 4 == 0 and yr % 100 != 0 or yr % 400 == 0:
  print(yr,"is leap year")
else:
  print(yr,"is not a leap year")