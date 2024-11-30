# Arithmetic operations program
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

sum_ = num1 + num2
diff = num1 - num2
prod = num1 * num2
int_quot = int(num1 // num2)
remainder = num1 % num2
frac_quot = num1 / num2

print(f"Numbers: {num1}, {num2}")
print(f"Sum: {sum_}")
print(f"Difference: {diff}")
print(f"Product: {prod}")
print(f"Integer Quotient: {int_quot}")
print(f"Remainder: {remainder}")
print(f"Fractional Quotient: {frac_quot:.2f}")
