#25. Write a program to check whether a triangle is equilateral, isosceles, or scalene.

a = int(input("Enter first side: "))
b = int(input("Enter second side: "))
c = int(input("Enter third side: "))

if a <= 0 or b <= 0 or c <= 0:
    print("Invalid sides")
elif a + b <= c or a + c <= b or b + c <= a:
    print("Not a valid triangle")
elif a == b and b == c:
    print("Equilateral triangle")
elif a == b or b == c or a == c:
    print("Isosceles triangle")
else:
    print("Scalene triangle")