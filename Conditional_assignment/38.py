# Write a program to check whether a student passed all subjects

name = input("Enter you'r name :- ")

sub_1 = int(input("Enter marks of sub 1 :- "))
sub_2 = int(input("Enter marks of sub 2 :- "))
sub_3 = int(input("Enter marks of sub 3 :- "))

if(sub_1 >= 40 and sub_2 >= 40 and sub_3 >= 40):
    print(f"congrats {name} you passed all the exam ")
else:
    print(f"sorry {name} you didn't pass sll the exams try again")