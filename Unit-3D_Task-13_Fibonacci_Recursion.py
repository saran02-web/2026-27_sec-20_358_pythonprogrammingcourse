def fibonacci(k):
    if k == 0:
        return 0
    if k == 1:
        return 1
    return fibonacci(k - 1) + fibonacci(k - 2)

n = int(input("Enter the number: "))
for i in range(n):
    print(fibonacci(i), end=" ")