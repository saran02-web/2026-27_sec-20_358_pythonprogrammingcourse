total_input_numbers = int(input("Enter how many numbers: "))
total_sum = 0

for _ in range(total_input_numbers):
    num = float(input("Enter a number: "))
    total_sum = total_sum + num

avg = total_sum / total_input_numbers

print("Sum of",total_input_numbers,"numbers is",total_sum)
print("Average of",total_input_numbers,"is",avg)
