#  Create a list and find the second largest number.


Numbers = [10, 50, 30, 50, 20, 40]
Unique = list(set(Numbers))
Unique.sort()

print("Second largest:", Unique[-2])
