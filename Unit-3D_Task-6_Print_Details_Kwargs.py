def print_details(**kwargs):
    for key, value in kwargs.item():
        print(f"{key}: {value}")
print_details(name="Ram", age=25, city="Krishna")
