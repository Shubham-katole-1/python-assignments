#Write a program to check whether a student is eligible for an exam (attendance + marks)

name = input("Enter student name :- ")
attandance = int(input("Enter Student attandance :- "))
marks = int(input("Enter student marks :- "))

if(attandance >= 75 and marks >= 50):
    print(f"{name} You are eligable for the exam ")
else:
    print(f"Sorry {name} you are not eligable for the exam")