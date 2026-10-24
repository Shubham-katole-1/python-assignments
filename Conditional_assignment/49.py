# Write a program to print result status using match case.

Status = input("Enter result status (pass, fail, pending): ")
Status = Status.lower()

match Status:
    case "pass":
        print("Congratulations! You passed")
    case "fail":
        print("You didn't make it this time")
    case "pending":
        print("Your result is pending")
    case _:
        print("Invalid status")