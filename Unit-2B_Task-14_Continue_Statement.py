n = int(input("Enter N (Print 1 to N, skip even numbers): "))
for i in range(1, n + 1):
    if i % 2 == 0:
        print("Skipping even number:",i)
        continue
    print("For loop odd number =",i)
