# Shipping Cost Calculator

## Input package weight and shipping rate
weight = float(input("Enter the package weight in kilograms: "))
rate = float(input("Enter the shipping rate per kilogram: "))

## Calculate shipping cost
shipping_cost = weight * rate


print(f"Weight: {weight}")
print(f"Rate: {rate}")
## Display the result
print(f"Shipping Cost: {shipping_cost} USD")

