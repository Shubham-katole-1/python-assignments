# Write a program to check grade based on marks (A, B, C, Fail).

Markes = int(input("Enter You'r markes :- "))
if(Markes >= 90):
    print("You got 'A' Grade")
elif(Markes >= 60):
    print("You got 'B' Grade")
elif(Markes >= 40):
    print("You got 'C' Grade")
else:
    print("You failed the Exam , Try again.")