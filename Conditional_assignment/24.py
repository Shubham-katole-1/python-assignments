# Write a program to check exam results (Distinction, First Class, Pass, Fail).

Marks = int(input("Enter your marks: "))

if (Marks >= 75):
    print("Distinction")
elif (Marks >= 60):
    print("First Class")
elif (Marks >= 40):
    print("Pass")
else:
    print("Fail")