n = int(input("Enter number: "))

if n < 1 or n > 100:
    print("Out of range")
elif n == 1:
    print("Not Prime")
elif n == 2 or n == 3 or n == 5 or n == 7:
    print("Prime")
elif n % 2 == 0 or n % 3 == 0 or n % 5 == 0 or n % 7 == 0:
    print("Not Prime")
else:
    print("Prime")
