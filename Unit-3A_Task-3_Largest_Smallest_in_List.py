user_data = input("Enter numbers separated by spaces: ")
lst_data = [int(x) for x in user_data.split()]

print("original : ", lst_data)
print(max(lst_data))
print(min(lst_data))
