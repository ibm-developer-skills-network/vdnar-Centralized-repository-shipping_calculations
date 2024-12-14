# Shipping Cost Calculator

## Input package weight and shipping rate
weight = float(input("Enter weight of the package in kilograms: "))
rate = float(input("Enter the shipping rate per kilogram: "))

## Calculate shipping cost
shipping_cost = weight * rate

## Display the result
print(f"Shipping Cost will be: {shipping_cost} USD")

