# Write a program to check user role (admin, user, guest) using match case

Role = input("Enter your role: ")
Role = Role.lower()

match Role:
    case "admin":
        print("You have administrator access")
    case "teacher":
        print("You can manage students")
    case "student":
        print("You can check your studies")
    case _:
        print("Unknown role")