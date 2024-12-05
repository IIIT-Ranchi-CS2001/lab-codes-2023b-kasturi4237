def my_zip(list1, list2, list3, strct=True):
    if strct:
        # Zipping only if all lists are of equal length
        if len(list1) == len(list2) == len(list3):
            return [(list1[i], list2[i], list3[i]) for i in range(len(list1))]
        else:
            raise ValueError("All lists must be of equal length for strict mode.")
    else:
        # Zipping using the minimum length
        min_length = min(len(list1), len(list2), len(list3))
        return [(list1[i], list2[i], list3[i]) for i in range(min_length)]

# Example usage
customer_names = ["Alice", "Bob", "Charlie"]
customer_ids = [101, 102, 103]
shopping_points = [150, 200, 120]
print(my_zip(customer_names, customer_ids, shopping_points, strct=True))
