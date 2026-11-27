number = int(input("Enter a 3-digit number: "))
original_number = number
armstrong_sum = 0
while number > 0:
    digit = number % 10
    armstrong_sum = armstrong_sum + digit**3
    number = number // 10
if armstrong_sum == original_number:
    print(original_number,"is an Armstrong number.")
else:
    print(original_number,"is not an Armstrong number.")
