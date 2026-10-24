# Write a program to check login status based on username and password.
Username = input("Enter username: ")
Password = input("Enter password: ")

if Username == "admin":
    if Password == "1234":
        print("Login successful")
    else:
        print("Incorrect password")
else:
    print("Incorrect username")