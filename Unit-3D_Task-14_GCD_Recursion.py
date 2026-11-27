def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)
x = int(input("Enter the number: "))
y = int(input("Enter the number: "))
print("GCD :", gcd(x, y))