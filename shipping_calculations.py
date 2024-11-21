# Updated Shipping Cost Calculator with Shipping Methods and Discount

def calculate_shipping_cost(weight, distance, shipping_method="Standard"):
    rate_per_kg = 5  # $ per kg for standard shipping
    rate_per_km = 0.1  # $ per km
    express_multiplier = 1.5  # Express shipping multiplier (1.5x for express)
    
    # Shipping method handling
    if shipping_method == "Express":
        rate_per_kg *= express_multiplier
        rate_per_km *= express_multiplier

    cost = (weight * rate_per_kg) + (distance * rate_per_km)

    # Apply discount if cost exceeds $100
    if cost > 100:
        discount = cost * 0.1  # 10% discount for orders over $100
        cost -= discount

    return cost

# Example usage
weight = float(input("Enter weight (in kg): "))
distance = float(input("Enter distance (in km): "))
shipping_method = input("Enter shipping method (Standard/Express): ").capitalize()

shipping_cost = calculate_shipping_cost(weight, distance, shipping_method)
print(f"The shipping cost is ${shipping_cost:.2f}")
