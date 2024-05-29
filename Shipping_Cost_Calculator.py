# Shipping Cost Calculator

## Input package weight and shipping rate
weight = float(input("Enter the package weight in kilograms: "))
rate = float(input("Enter the shipping rate per kilogram: "))

## Calculate shipping cost
shipping_cost = weight * rate
tax = shipping_cost*13/100
shipping_cost += tax

## Display the result
print(f"Shipping Cost: {shipping_cost} USD")

