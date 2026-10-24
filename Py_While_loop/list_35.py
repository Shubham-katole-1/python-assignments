# Create a list and remove all even numbers.


Numbers = [1, 2, 3, 4, 5, 6, 7, 8]

Result = []

for i in Numbers:
    if i % 2 != 0:
        Result.append(i)

print(Result)
