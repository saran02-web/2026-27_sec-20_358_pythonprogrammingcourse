rows = int(input("Enter grid size (rows & columns): "))
for row_loop_var in range(1, rows + 1):
    for column_loop_var in range(1, rows + 1):
        print("*", end=" ")
    print()
