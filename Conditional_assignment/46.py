#Write a program to print grade description using match case
Grade = input("Enter your grade (A, B, C, F): ")
Grade = Grade.upper()

match Grade:
    case "A":
        print("You got Excellent grade")
    case "B":
        print("You performed Very Good")
    case "C":
        print("it was Good")
    case "F":
        print("You got to prepare for it once more")
    case _:
        print("Invalid grade")