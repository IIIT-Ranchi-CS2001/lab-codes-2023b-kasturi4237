# Equivalent impedance program
z1_real, z1_imag = map(float, input("Enter real and imaginary parts of Z1: ").split())
z2_real, z2_imag = map(float, input("Enter real and imaginary parts of Z2: ").split())

Z1 = complex(z1_real, z1_imag)
Z2 = complex(z2_real, z2_imag)

Z_eq = (Z1 * Z2) / (Z1 + Z2)

print(f"Z1: {Z1}, Z2: {Z2}")
print(f"Equivalent Impedance: {Z_eq}")
print(f"Real Part: {Z_eq.real}")
print(f"Imaginary Part: {Z_eq.imag}")
