#Write a program to calculate electricity bill based on units consumed.

Units = int(input("Enter electricity units: "))

if Units >= 0:
    Bill = Units * 5
    print("Your electricity bill is Rs.", Bill)
else:
    print("Invalid units")