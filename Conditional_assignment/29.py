# Write a program to check blood donation eligibility based on age and weight.

Age = int(input("Enter your age: "))
Weight = float(input("Enter your weight in kg: "))

if Age >= 18 and Weight >= 50:
    print("You Meets basic age and weight criteria you can donate you'r blood")
else:
    print("You Does not meet basic criteria, you can't donate blood.")