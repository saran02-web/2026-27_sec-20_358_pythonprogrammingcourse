n = int(input("Enter N (Print until N, stop early at 5): "))
for i in range(1, n + 1):
    if i == 5:
        print("Breaking for loop at number",i,"N was",n)
        break
    print("for loop number =",i,"up to",n)
