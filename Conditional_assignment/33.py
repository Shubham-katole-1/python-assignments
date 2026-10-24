#  Write a program to check whether a person can apply for a loan
salary = int(input("Enter you'r salary :- "))
score = int(input("Enter you'r credit score :- "))

if (salary >= 25000 and score >= 600) :
    print("You can apply for a loan")
else:
    print("Sorry,You can't apply for a loan")