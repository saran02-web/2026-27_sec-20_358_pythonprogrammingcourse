for i in range(1, rows + 1):
    # Print leading spaces to center the triangle
    for space in range(1, rows - i + 1):
        print(" ", end=" ")
        
    value = 1
    for j in range(1, i + 1):
        print(value, end=" ")
        # Calculate the next binomial coefficient in the row
        value = value * (i - j) // j
        
    print()
