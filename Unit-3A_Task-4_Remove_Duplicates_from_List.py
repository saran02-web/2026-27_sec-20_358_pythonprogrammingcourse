user_data = input("Enter the numbers separated by spaces: ")
lst_data = [int(x) for x in user_data.split()]

print("Original : ", lst_data)

unique = []
for item in lst_data:
    if item not in unique:
        unique.append(item)

print("Without duplicates : ", unique)
