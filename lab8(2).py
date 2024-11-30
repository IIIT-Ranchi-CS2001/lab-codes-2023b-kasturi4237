import numpy as np

# Step 1: User inputs the shapes of the two 3D arrays
try:
    shape1 = tuple(map(int, input("Enter the dimensions for the first 3D array (e.g., 2 3 4): ").split()))
    shape2 = tuple(map(int, input("Enter the dimensions for the second 3D array (e.g., 2 3 4): ").split()))

    # Step 2: Create the arrays with random integers
    A1 = np.random.randint(1, 101, size=shape1)  # Random integers between 1 and 100
    A2 = np.random.randint(1, 101, size=shape2)

    print("\nArray A1:")
    print(A1)
    print("\nArray A2:")
    print(A2)

    # Step 3: Select elements divisible by 5 from A1
    A1_divisible_by_5 = A1[A1 % 5 == 0]
    print("\nElements of A1 divisible by 5:")
    print(A1_divisible_by_5)

    # Step 4: Select elements divisible by 4 from A2
    A2_divisible_by_4 = A2[A2 % 4 == 0]
    print("\nElements of A2 divisible by 4:")
    print(A2_divisible_by_4)

    # Step 5: Join the two arrays to form a single-dimensional array
    joined_array = np.concatenate((A1_divisible_by_5, A2_divisible_by_4))
    print("\nJoined 1D array:")
    print(joined_array)

    # Step 6: Construct the largest possible square matrix
    n = int(np.floor(np.sqrt(joined_array.size)))  # Determine the size of the square matrix
    square_matrix = joined_array[:n * n].reshape(n, n)  # Reshape the appropriate number of elements into a square matrix

    print("\nLargest possible square matrix:")
    print(square_matrix)

except ValueError:
    print("Invalid input! Please enter valid dimensions.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
