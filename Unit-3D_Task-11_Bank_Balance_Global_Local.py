balance = 1000
def deposit(amount):
    global balance  
    balance += amount
    print("Deposited:", amount)
    print("Updated global balance:", balance)
def show_local_balance():
    balance = 500 
    print("Local balance inside function:", balance)
print("Initial global balance:", balance)
deposit(500)
show_local_balance()
print("Final global balance:", balance)