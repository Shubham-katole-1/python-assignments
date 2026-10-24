#Write a program to build a simple ATM menu using a match case

print("1. Check Balance")
print("2. Deposit Money")
print("3. Withdraw Money")
print("4. Exit")

Choice = int(input("Enter your choice: "))

match Choice:
    case 1:
        print("Your balance is Rs. 5000")
    case 2:
        print("Deposit option selected")
    case 3:
        print("Withdrawal option selected")
    case 4:
        print("Thank you for using the ATM")
    case _:
        print("Invalid choice")