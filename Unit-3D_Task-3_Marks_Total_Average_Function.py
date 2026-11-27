def total_and_average(mark_1, mark_2, mark_3):
    total = mark_1 + mark_2 + mark_3
    average = total / 3
    return total, average
m1 = int(input("Enter first mark: "))
m2 = int(input("Enter second mark: "))
m3 = int(input("Enter third mark: "))
total_marks, avg_marks = total_and_average(m1, m2, m3)
print("Total:", total_marks)
print("Average:", avg_marks)
