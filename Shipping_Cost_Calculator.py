# Shipping Cost Calculator

## Input package weight and shipping rate
weight = float(input("Enter the package weight in kilograms: "))
rate = float(input("Enter the shipping rate per kilogram: "))

## Calculate shipping cost
shipping_cost = weight * rate

#converting rates
print(f"Shipping Cost: {shipping_cost * 3.76} AED")

## Display the result
print(f"Shipping Cost: {shipping_cost} USD")

