rows = int(input("Enter the no of rows: "))
for r in range(1, rows + 1):
    for s in range(1, rows - r + 1):
        print(" ", end="")
    for c in range(1, 2 * r):
        print(c, end="")
    print()
