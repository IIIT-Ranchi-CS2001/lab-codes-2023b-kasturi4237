import math

# Input coefficients
a = int(input("Enter coefficient a: "))
b = int(input("Enter coefficient b: "))
c = int(input("Enter coefficient c: "))

discriminant = b**2 - 4*a*c

if discriminant == 0:
    root = -b / (2*a)
    print(f"Repeated Root: {root}")
elif discriminant > 0:
    root1 = (-b + math.sqrt(discriminant)) / (2*a)
    root2 = (-b - math.sqrt(discriminant)) / (2*a)
    print(f"Distinct Real Roots: {root1}, {root2}")
else:
    real_part = -b / (2*a)
    imag_part = math.sqrt(-discriminant) / (2*a)
    print(f"Complex Roots: {real_part} ± {imag_part}i")
