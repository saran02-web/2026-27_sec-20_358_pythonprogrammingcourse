rows = int(input("Enter number of rows: "))
for r in range(rows, 0, -1):
    for c in range(1, r + 1):
        print("*", end=" ")
    print()
