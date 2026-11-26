rows = int(input("Enter the number of rows: "))
symbol = input("Enter symbol to print (e.g., * or 0): ")
for r in range(1, rows + 1):
    for c in range(1, r + 1):
        print(symbol, end=" ")
    print()