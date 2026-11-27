a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
print("Before:", a, b)
a, b = b, a
print("After:", a, b)
