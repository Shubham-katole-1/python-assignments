#Write a program to find the smallest of three numbers
A = int(input("Enter Your First Number :- "))
B = int(input("Enter Your Second Number :- "))
C = int(input("Enter Your Third Number :- "))

if (A <= B and A <= C) :
    print(f"First Number is smallest:- {A}")
elif (B <= A and B <= C):
    print(f"Second number is smallest:- {B}")
else:
    print(f"Third number is smallest:- {C}")