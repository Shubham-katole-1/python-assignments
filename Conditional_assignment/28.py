# Write a program to calculate discounts based on total shopping amount.

Amount = int(input("Enter shopping amount: "))

if Amount < 0:
    print("Invalid amount")
elif Amount >= 5000:
    Discount = Amount * 20 / 100
    print("Discount: Rs.", Discount)
elif Amount >= 2000:
    Discount = Amount * 10 / 100
    print("Discount: Rs.", Discount)
else:
    print("No discount")