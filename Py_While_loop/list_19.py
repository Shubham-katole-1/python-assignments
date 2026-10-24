#Create a list of 10 numbers and remove duplicates. 


Numbers = [10, 20, 10, 30, 20, 40, 50, 30, 60, 10]

Unique = []

for i in Numbers:
    if i not in Unique:
        Unique.append(i)

print(Unique)
