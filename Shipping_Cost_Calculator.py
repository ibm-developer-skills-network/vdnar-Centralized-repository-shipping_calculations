# Shipping Cost Calculator

## Input package weight and shipping rate
weight = float(input("Enter the package weight in kilograms: "))
rate = float(input("Enter the shipping rate per kilogram: "))
additional_cost=float(input("Enter the additional_cost"))

## Calculate shipping cost
shipping_cost = weight * rate + additional_cost

## Display the result
print(f"Shipping Cost: {shipping_cost} USD")

