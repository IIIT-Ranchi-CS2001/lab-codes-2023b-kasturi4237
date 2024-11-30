import numpy as np

# Define the coefficients matrix (ticket prices for each event)
coefficients = np.array([
    [44, 38, 21],  # Roller Coaster
    [32, 28, 15],  # 4D Max Cinema
    [24, 20, 10]   # Cable Car
])

# Define the totals vector (total money spent on each event)
totals = np.array([1412, 1024, 728])

try:
    # Solve the system of linear equations
    solution = np.linalg.solve(coefficients, totals)
    
    # Extract the solution
    males, females, kids = solution
    
    print("Number of males:", int(males))
    print("Number of females:", int(females))
    print("Number of kids:", int(kids))
except np.linalg.LinAlgError as e:
    print("Error: The system of equations could not be solved:", e)
except Exception as e:
    print("An unexpected error occurred:", e)
