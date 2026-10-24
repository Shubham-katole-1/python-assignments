#10. Write a program to check whether a number is a single-digit number or not.

num = int(input("Enter a number: "))

if num >= -9 and num <= 9:
    print("You'r Entered Number is Single-digit number")
else:
    print("You'r Enterd Number is Not a single-digit number")