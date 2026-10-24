#Write a program to print the day name based on day number (1–7).

Day = int(input("Enter the number of day(1 - 7) :- "))

if(Day == 1) :
    print("Sunday")
elif(Day == 2) :
    print("Monday")
elif(Day == 3):
    print("Tuesday")
elif(Day == 4):
    print("Wenesday")
elif(Day == 5):
    print("Thursday")
elif(Day == 6):
    print("Friday")
elif(Day == 7):
    print("Satuerday")
else:
    print("Please enter a correct number")