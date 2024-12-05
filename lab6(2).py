def my_sort(data, key=0):
    for i in range(len(data)):
        for j in range(len(data) - i - 1):
            if data[j][key] > data[j + 1][key]:
                data[j], data[j + 1] = data[j + 1], data[j]
    return data

# Example usage
zipped_data = [("Alice", 101, 150), ("Bob", 102, 200), ("Charlie", 103, 120)]
print(my_sort(zipped_data, key=0))  # Sort by customer name
print(my_sort(zipped_data, key=1))  # Sort by customer ID
print(my_sort(zipped_data, key=2))  # Sort by shopping points
