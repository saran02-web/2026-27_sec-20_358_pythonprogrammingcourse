user_input = input("Enter numbers separated by spaces: ")
lst_data = [int(x) for x in user_input.split()]
print("List:", lst_data)
print("Elements in the list:")
for item in lst_data:
    print(item)
