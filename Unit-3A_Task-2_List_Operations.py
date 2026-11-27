user_data = input("Enter numbers separated by spaces: ")
lst_data = [int(x) for x in user_data.split()]

print("list : ", lst_data)

lst_data.append(9)
print("After append : ", lst_data)

lst_data.insert(0, 7)
print("After insert : ", lst_data)

lst_data.remove(1)
print("After remove : ", lst_data)

lst_data.sort()
print("After sort : ", lst_data)

lst_data.reverse()
print("After reverse : ", lst_data)
