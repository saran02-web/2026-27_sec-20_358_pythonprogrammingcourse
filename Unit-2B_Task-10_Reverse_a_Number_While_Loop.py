counter = 0  

def increment_counter():
    global counter  
    counter += 1
    print("Counter inside function:", counter)

print("Initial counter:", counter)

increment_counter()
increment_counter()
increment_counter()

print("Final counter:", counter)
