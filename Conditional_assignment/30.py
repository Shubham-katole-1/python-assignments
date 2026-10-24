#. Write a program to check the type of number (single, double, or three digit).

Num = int(input("Enter your number: "))

if Num >= -9 and Num <= 9:
    print("You entered a single-digit number")

elif Num >= -99 and Num <= 99:
    print("You entered a double-digit number")

elif Num >= -999 and Num <= 999:
    print("You entered a triple-digit number")

else:
    print("You entered a number with more than three digits")