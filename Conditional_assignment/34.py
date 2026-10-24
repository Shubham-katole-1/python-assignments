# Write a program to check whether a year is a leap year and century year.

Year = int(input("Enter a year: "))

if Year % 100 == 0:
    print("Century year")

    if Year % 400 == 0:
        print("Leap year")
    else:
        print("Not a leap year")
elif Year % 4 == 0:
    print("Leap year")
else:
    print("Not a leap year")