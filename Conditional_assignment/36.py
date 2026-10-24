#Write a program to check whether a person is eligible for a driving license

name = input("Enter you'r name :- ")
age = int(input("Enter you'r age :- "))

if(age >= 18):
    print(f"{name} You can aaply for a driving licence.")
else:
    print(f"sorry {name} you can't apply for a driving licence")

