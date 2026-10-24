# Write a program to check salary bonus based on years of service.

salary = int(input("Enter your salary: "))
service = int(input("Enter years of service: "))

if (service <= 2):
    bonus = salary * 10 / 100
elif (service < 5):
    bonus = salary * 50 / 100
elif (service < 10):
    bonus = salary * 75 / 100
else:
    bonus = salary * 100 / 100

print("Your bonus is Rs.", bonus)