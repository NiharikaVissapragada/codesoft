def calc():
    
    n1 = float(input("Enter the first number: "))
    n2 = float(input("Enter the second number: "))
    
    print("Choose an operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")

    operation = input("Enter the number corresponding to the operation (1/2/3/4): ")

    if operation == '1':
        result = n1 + n2
        print(f"{n1} + {n2} = {result}")
    elif operation == '2':
        result = n1 - n2
        print(f"{n1} - {n2} = {result}")
    elif operation == '3':
        result = n1 * n2
        print(f"{n1} * {n2} = {result}")
    elif operation == '4':
        if n2 != 0:
            result = n1 / n2
            print(f"{n1} / {n2} = {result}")
        else:
            print(" Cannot divide by zero.")
    else:
        print("Invalid.")

calc()