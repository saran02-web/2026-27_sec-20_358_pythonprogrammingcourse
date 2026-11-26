x = int(input("enter first number: "))
y = int(input("enter second number: "))
z = int(input("enter third number: "))
if x <= y and x <= z:
    smallest = x
elif y <= x and y <= z:
    smallest = y
else:
    smallest = z
print("Smallest of three numbers is:", smallest)