# Shipping Cost Calculator

# Here is a new update by Prasad2357

## Input package weight and shipping rate
weight = float(input("Enter the package weight in kilograms: "))
rate = float(input("Enter the shipping rate per kilogram: "))

## Calculate shipping cost
shipping_cost = weight * rate

## Display the result
print(f"Shipping Cost: {shipping_cost} USD")

## Display the result in INR
shipping_cost=shipping_cost/0.8
print(f"Shipping Cost: {shipping_cost} INR")

