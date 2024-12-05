import matplotlib.pyplot as plt
import numpy as np
import math

# Generate K random numbers within a limit N
def generate_random_numbers(K, N):
    if K < 10:
        raise ValueError("Minimum value of K should be 10.")
    return np.random.randint(1, N+1, size=K)

# Function to separate prime and composite numbers
def separate_prime_composite(numbers):
    primes = []
    composites = []
    for num in numbers:
        if num < 2:
            composites.append(num)
        elif all(num % i != 0 for i in range(2, int(math.sqrt(num)) + 1)):
            primes.append(num)
        else:
            composites.append(num)
    return primes, composites

# User input for K and N
K = int(input("Enter the number of random numbers (K, minimum 10): "))
N = int(input("Enter the upper limit (N): "))

# Generate numbers and separate into primes and composites
try:
    random_numbers = generate_random_numbers(K, N)
    primes, composites = separate_prime_composite(random_numbers)

    # Calculate squares of primes and square roots of composites
    prime_squares = [p**2 for p in primes]
    composite_roots = [math.sqrt(c) for c in composites]

    # Scatter plots
    fig, axes = plt.subplots(1, 2, figsize=(12, 6))

    # Prime numbers vs their squares
    axes[0].scatter(primes, prime_squares, color='blue', label="Prime Numbers")
    axes[0].set_title("Prime Numbers vs Squares")
    axes[0].set_xlabel("Prime Numbers")
    axes[0].set_ylabel("Squares")
    axes[0].legend()

    # Composite numbers vs their square roots
    axes[1].scatter(composites, composite_roots, color='green', label="Composite Numbers")
    axes[1].set_title("Composite Numbers vs Square Roots")
    axes[1].set_xlabel("Composite Numbers")
    axes[1].set_ylabel("Square Roots")
    axes[1].legend()

    plt.tight_layout()
    plt.show()

except ValueError as e:
    print(e)
