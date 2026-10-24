#Write a program to perform calculator operations using match case
A = float(input("Enter first number: "))
B = float(input("Enter second number: "))
Operator = input("Enter operator (+, -, *, /): ")

match Operator:
    case "+":
        print("Result:", A + B)
    case "-":
        print("Result:", A - B)
    case "*":
        print("Result:", A * B)
    case "/":
        if B != 0:
            print("Result:", A / B)
        else:
            print("Cannot divide by zero")
    case _:
        print("Invalid operator")