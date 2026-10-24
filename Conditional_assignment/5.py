# Write a program to check whether a given year is a leap year or not.


Year = int(input("Enter a year: "))

if Year % 400 == 0:
    print("It's a Leap year")
elif Year % 100 == 0:
    print("It's Not a leap year")
elif Year % 4 == 0:
    print("It's Leap year")
else:
    print("It's Not a leap year")
