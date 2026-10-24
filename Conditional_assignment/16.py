#  Write a program to find the greatest of three numbers.
Num_1 = int(input("Enter you'r First Number :- "))
Num_2 = int(input("Enter you'r Second Number :- "))
Num_3 = int(input("Enter you'r Third Number :- "))
if(Num_1 > Num_2 and Num_1 > Num_3):
    print("First Number is Greatest")
elif(Num_2 > Num_1 and Num_2 > Num_3):
    print("Second number is Greatest")
else:
    print("Third number is Greatest")