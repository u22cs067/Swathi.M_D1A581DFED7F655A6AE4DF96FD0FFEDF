def linear_search_product(product_list, target_product_name):
    # Initialize an empty list to store indices of occurrences
    indices = []

    # Iterate through the product list
    for index, product in enumerate(product_list):
        if product["name"] == target_product_name:
            # If the product name matches the target, add the index to the list
            indices.append(index)

    return indices

# Test the function
if __name__ == "__main__":
    # Sample list of products (each product is represented as a dictionary)
    products = [
        {"name": "Product A", "price": 10.99},
        {"name": "Product B", "price": 19.99},
        {"name": "Product A", "price": 15.99},
        {"name": "Product C", "price": 25.99},
        {"name": "Product A", "price": 12.99},
    ]

    target_product_name = "Product A"
    
    # Perform a linear search for the target product name
    result_indices = linear_search_product(products, target_product_name)

    if result_indices:
        print(f"The target product '{target_product_name}' was found at indices: {result_indices}")
    else:
        print(f"The target product '{target_product_name}' was not found in the list.")