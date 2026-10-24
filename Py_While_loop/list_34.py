# Create a list and find common elements between two lists. 


List1 = [10, 20, 30, 40]
List2 = [30, 40, 50, 60]

Common = []

for i in List1:
    if i in List2:
        Common.append(i)

print(Common)
