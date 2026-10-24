#. Write a program to check whether a password is valid using nested if

Username = input("Enter username: ")

if Username == "admin":
    Password = input("Enter password: ")

    if Password == "12345678":
        print("Login successful")
    else:
        print("Incorrect password")
else:
    print("Incorrect username")