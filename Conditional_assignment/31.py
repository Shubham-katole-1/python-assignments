#Write a program to check whether a number is  0 positive and even using nested if

Num = int(input("Enter a number: "))

if Num > 0:
    if Num % 2 == 0:
        print("Enterd Number is Positive and even number")
    else:
        print("Positive but odd number")
else:
    print("Enterd Number is not positive")
