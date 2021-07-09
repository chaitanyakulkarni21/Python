#Menu Driven Calculator program using if else and while loop 
while True:
    print("Menu: ")
    print("1. Sum")
    print("2. Difference")
    print("3. Product")
    print("4. Division")
    print("5. Exit\n")
    
    n = int(input("Choose an option: "))
    if n == 1:
        x = int(input("Enter num 1 : "))
        y = int(input("Enter num 2: "))
        print("Sum = ",x+y,"\n")
        #break
    elif n == 2:
        x = int(input("Enter num 1 : "))
        y = int(input("Enter num 2: "))
        print("Difference = ",x-y,"\n")
        #break
    elif n == 3:
        x = int(input("Enter num 1 : "))
        y = int(input("Enter num 2: "))
        print("Product = ",x*y,"\n")
        #break
    elif n == 4:
        x = int(input("Enter num 1 : "))
        y = int(input("Enter num 2: "))
        print("Remainder = ",x/y)
        print("Quotient = ", x%y,"\n")
        #break
    else:
        print("You are out of the Menu...")
        break
        