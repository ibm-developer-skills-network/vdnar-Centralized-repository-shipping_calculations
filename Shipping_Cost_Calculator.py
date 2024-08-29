# Here is a new update by vaishnavinkm

# Shipping Cost Calculator

## Input package weight and shipping rate
try:
weight = float(input("Enter the package weight in kilograms: "))
rate = float(input("Enter the shipping rate per kilogram: "))
except ValueError:
    print("Invalid input. Please enter numeric values.")
    exit()
## Calculate shipping cost
shipping_cost = weight * rate

## Display the result
print(f"Shipping Cost: {shipping_cost} USD")

