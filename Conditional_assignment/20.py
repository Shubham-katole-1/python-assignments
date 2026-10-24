#Write a program to check ticket price based on age.

Age = int(input("Enter you'r age :- "))
if(Age <= 5):
    print("You'r ticket is free")
elif(Age <= 18 ):
    print("You will pay the half price: Rs.50")
elif(Age < 50):
    print("You will pay the full price: Rs.100")
else:
    print("Senior ticket price is : Rs.50")
