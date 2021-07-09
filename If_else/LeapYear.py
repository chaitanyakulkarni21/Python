# Check whether an entered year is leap year or not

year = int(input("Enter any year: "))
if year % 4 == 0 or year % 400 == 0:
    print("Leap Year")
else:
    print("Not a leap Year")
