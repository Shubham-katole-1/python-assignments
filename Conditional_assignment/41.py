#Write a program to print weekday name using match case

Day = int(input("Enter day number (1-7): "))

match Day:
    case 1:
        print("Sunday")
    case 2:
        print("Monday")
    case 3:
        print("Tuessday")
    case 4:
        print("Wensday")
    case 5:
        print("Thurstday")
    case 6:
        print("Friday")
    case 7:
        print("Saturday")
    case _:
        print("Invalid day number")