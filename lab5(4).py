# Input the lists
customer_names = [input(f"Enter name for customer {i+1}: ") for i in range(3)]
customer_ids = [int(input(f"Enter ID for customer {i+1}: ")) for i in range(3)]
shopping_points = [int(input(f"Enter shopping points for customer {i+1}: ")) for i in range(3)]

# With zip()
zipped_list = list(zip(customer_names, customer_ids, shopping_points))
print("List of tuples using zip():", zipped_list)

# Without zip()
manual_list = [(customer_names[i], customer_ids[i], shopping_points[i]) for i in range(len(customer_names))]
print("List of tuples without zip():", manual_list)
