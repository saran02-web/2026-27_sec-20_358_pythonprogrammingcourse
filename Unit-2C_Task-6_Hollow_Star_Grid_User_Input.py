rows = int(input("Enter grid size (rows & columns): "))
for r in range(1, rows + 1):
    for c in range(1, rows + 1):
        if r == 1 or r == rows or c == 1 or c == rows:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
