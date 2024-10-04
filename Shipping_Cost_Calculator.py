# Shipping Cost Calculator

## Input package weight and shipping rate
weight = float(input("Enter the package weight in Pounds: "))
rate = float(input("Enter the shipping rate per Kilograms: "))

## Calculate shipping cost
shipping_cost = weight * rate * 2.2

## Display the result
print(f"Shipping Cost: {shipping_cost} USD")

