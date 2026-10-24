# Create a list and demonstrate all list methods. 


Numbers = list(map(int, input("Enter numbers separated by space: ").split()))  # Take numbers from user and convert them into a list

print("Original List:", Numbers)  # Display the original list

# 1. append()

Num = int(input("Enter a number to append: "))
Numbers.append(Num)  # Add a number at the end of the list
print("After append:", Numbers)


# 2. insert()

Num = int(input("Enter a number to insert: "))
Pos = int(input("Enter the position to insert: "))
Numbers.insert(Pos, Num)  # Insert a number at the given index
print("After insert:", Numbers)


# 3. extend()

More = list(map(int, input("Enter more numbers to extend: ").split()))
Numbers.extend(More)  # Add all elements of another list
print("After extend:", Numbers)


# 4. remove()

Num = int(input("Enter a number to remove: "))
if Num in Numbers:
    Numbers.remove(Num)  # Remove the first matching value from the list
    print("After remove:", Numbers)
else:
    print("Number not found in the list")


# 5. pop()

Pos = int(input("Enter index to pop: "))
if -len(Numbers) <= Pos < len(Numbers):
    Numbers.pop(Pos)  # Remove and return the element at the given index
    print("After pop:", Numbers)
else:
    print("Invalid index")


# 6. index()

Num = int(input("Enter a number to find its index: "))
if Num in Numbers:
    print("Index:", Numbers.index(Num))  # Find the index of the first matching value
else:
    print("Number not found")


# 7. count()

Num = int(input("Enter a number to count: "))
print("Count:", Numbers.count(Num))  # Count how many times a number appears


# 8. sort()

Numbers.sort()  # Sort the list in ascending order
print("After sort:", Numbers)


# 9. reverse()

Numbers.reverse()  # Reverse the current order of the list
print("After reverse:", Numbers)


# 10. copy()

New_List = Numbers.copy()  # Create a separate shallow copy of the list
print("Copied List:", New_List)


# 11. clear()

Choice = input("Do you want to clear the copied list? (yes/no): ")
if Choice.lower() == "yes":
    New_List.clear()  # Remove all elements from the copied list
    print("After clear:", New_List)


# 12. len()

print("Total elements:", len(Numbers))  # Count the total number of elements


# 13. sum()

print("Sum:", sum(Numbers))  # Calculate the sum of all numbers


# 14. max()

if len(Numbers) > 0:
    print("Maximum:", max(Numbers))  # Find the largest number in the list


# 15. min()

if len(Numbers) > 0:
    print("Minimum:", min(Numbers))  # Find the smallest number in the list


# 16. sorted()

Sorted_List = sorted(Numbers)  # Create a new sorted list without changing Numbers
print("Sorted List:", Sorted_List)


# 17. reversed()

Reverse_List = list(reversed(Numbers))  # Create a reversed copy using reversed()
print("Reversed List:", Reverse_List)


# 18. any()

print("Any non-zero number:", any(Numbers))  # Check whether at least one element is truthy


# 19. all()

print("All numbers are non-zero:", all(Numbers))  # Check whether every element is truthy


# 20. list()

Another_List = list(Numbers)  # Create another list from the existing list
print("Another List:", Another_List)
