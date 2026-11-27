def calculate_sum(*args):
    total = 0
    for num in args:
        total += num
    return total
print("Sum of 2 numbers (10, 20):", calculate_sum(10, 20))
print("Sum of 4 numbers (5, 10, 15, 20):", calculate_sum(5, 10, 15, 20))
print("Sum with no arguments:", calculate_sum())
