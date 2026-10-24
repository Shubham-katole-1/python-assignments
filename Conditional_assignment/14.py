#. Write a program to check whether a given character is uppercase or lowercase

Char = input("Enter You'r Character :- ")
if Char.isupper():
    print("It's a Uppercase char")
elif Char.islower():
    print("It's a lowercase")
else:
    print("It's not a Uppercase and lowecase")