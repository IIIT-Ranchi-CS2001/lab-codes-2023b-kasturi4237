import math
import random

# Generate two points in 3D space
point1 = tuple(random.randint(-100, 100) for _ in range(3))
point2 = tuple(random.randint(-100, 100) for _ in range(3))

# Calculate Euclidean distance
def euclidean_distance(p1, p2):
    return math.sqrt(sum((p1[i] - p2[i])**2 for i in range(3)))

# Display points and distance
print(f"Point 1: {point1}")
print(f"Point 2: {point2}")
distance = euclidean_distance(point1, point2)
print(f"Euclidean Distance: {distance:.2f}")
