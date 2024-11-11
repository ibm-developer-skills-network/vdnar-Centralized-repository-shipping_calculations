# Shipping Cost Calculator

# Function to get valid input
def get_valid_input(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value <= 0:
                print("Value must be greater than 0. Please try again.")
            else:
                return value
        except ValueError:
            print("Invalid input! Please enter a valid number.")

# Get package weight and shipping rate from the user with validation
weight = get_valid_input("Enter the package weight in kilograms: ")
rate = get_valid_input("Enter the shipping rate per kilogram (in USD): ")

# Optional: Add a distance factor for the shipping cost calculation (e.g., shipping based on distance)
distance = get_valid_input("Enter the shipping distance in kilometers: ")

# Calculate the basic shipping cost
shipping_cost = weight * rate

# Add an extra fee based on distance (for example: $0.50 per km)
distance_fee = distance * 0.5
total_cost = shipping_cost + distance_fee

# Optional: Apply discount for high shipping costs (e.g., more than $100)
if total_cost > 100:
    discount = total_cost * 0.1  # 10% discount
    total_cost -= discount
    print(f"Applied a 10% discount of {discount:.2f} USD")

# Display the result with clear formatting
print(f"\nShipping Details:")
print(f"Package Weight: {weight} kg")
print(f"Shipping Rate: {rate} USD per kg")
print(f"Distance: {distance} km")
print(f"Base Shipping Cost: {shipping_cost:.2f} USD")
print(f"Distance Fee: {distance_fee:.2f} USD")
print(f"Total Shipping Cost: {total_cost:.2f} USD")
