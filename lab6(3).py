def my_max(*args):
    if not args:
        raise ValueError("No elements provided.")
    max_value = args[0]
    for item in args:
        if item > max_value:
            max_value = item
    return max_value

# Example usage
print(my_max(*[1, 5, 9, 2]))        # List
print(my_max(*{10, 30, 20}))        # Set
print(my_max(*(7, 3, 5, 12)))       # Tuple
