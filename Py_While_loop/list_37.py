#  Create a list and check palindrome list.

Numbers = input("Enter numbers separated by spaces: ").split()

if Numbers == Numbers[::-1]:
    print("Palindrome list")
else:
    print("Not a palindrome list")