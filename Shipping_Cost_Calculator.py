# Shipping Cost Calculator

## Input package weight and shipping rate
weight = float(input("Enter the package weight in kilograms: "))
rate = float(input("Enter the shipping rate per kilogram: "))

## Calculate shipping cost
ship_cost = weight * rate

## Display the result
print(f"Shipping Cost: {ship_cost} USD")

