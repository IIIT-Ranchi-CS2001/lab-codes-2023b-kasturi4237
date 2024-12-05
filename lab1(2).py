import math

# Input sides of the triangle
a, b, c = map(float, input("Enter the three sides of the triangle (a b c): ").split())

# Calculate area using Heron's formula
s = (a + b + c) / 2
area = math.sqrt(s * (s - a) * (s - b) * (s - c))

# Calculate perimeter
perimeter = a + b + c

# Calculate angles
angle_A = math.degrees(math.acos((b**2 + c**2 - a**2) / (2 * b * c)))
angle_B = math.degrees(math.acos((a**2 + c**2 - b**2) / (2 * a * c)))
angle_C = 180 - angle_A - angle_B

print(f"Sides: a={a}, b={b}, c={c}")
print(f"Area: {area:.2f}")
print(f"Perimeter: {perimeter}")
print(f"Angles: A={angle_A:.2f}°, B={angle_B:.2f}°, C={angle_C:.2f}°")
