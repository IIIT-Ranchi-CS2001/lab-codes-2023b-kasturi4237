import numpy as np

def Create_Array(*args):
    """
    Creates a square array with the given arguments as diagonal elements and 
    zeros elsewhere.
    
    Args:
        *args: Variable number of arguments to form the diagonal of the array.

    Returns:
        numpy.ndarray: A square array with diagonal elements as specified by `args`.
    """
    # Convert the input arguments into a numpy array to form the diagonal
    diagonal_elements = np.array(args)
    
    # Create a square matrix with the diagonal elements
    square_array = np.diag(diagonal_elements)
    
    return square_array

# Example usage
if __name__ == "__main__":
    # Create an array with specified diagonal elements
    result = Create_Array(1, 2, 3, 4)
    print("Generated Array:")
    print(result)
