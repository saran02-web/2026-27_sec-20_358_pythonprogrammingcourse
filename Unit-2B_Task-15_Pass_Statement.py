n = int(input("Enter N (use pass for multiples of 3): "))
for i in range(1, n + 1):
    if i % 3 == 0:
        print("Used pass for multiple of 3: ",i,"N is",n)
    else:
        print("For loop number = ",i,"up to ",n)