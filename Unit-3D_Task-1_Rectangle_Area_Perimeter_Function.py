def rectangle_area_perimeter(length, breadth):
    area = length * breadth
    perimeter = 2 * (length + breadth)
    return area, perimeter


length = float(input("enter length: "))
breadth = float(input("enter breadth: "))

area, perimeter = rectangle_area_perimeter(length, breadth)

print("area :", area)
print("perimeter :", perimeter)
