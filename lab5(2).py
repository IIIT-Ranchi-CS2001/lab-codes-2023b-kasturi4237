# Input the coordinates of two points
point1 = [int(i) for i in input("Enter coordinates of Point 1 (x1 y1): ").split()]
point2 = [int(i) for i in input("Enter coordinates of Point 2 (x2 y2): ").split()]

# Calculate the slope
try:
    slope = (point2[0] - point1[0]) / (point2[1] - point1[1])
    print(f"Equation of the straight line: (x - {point1[0]}) = {slope:.2f} * (y - {point1[1]})")
except ZeroDivisionError:
    print("The line is vertical: x = ", point1[0])
