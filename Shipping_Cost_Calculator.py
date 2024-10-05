# Here is a new update by milarodcar, just trying to make this work
# Never gonna give you up, never gonna shot you done. Never gonnat turn arounda and hurt you
# Shipping Cost Calculator

## Input package weight and shipping rate
weight = float(input("Enter the package weight in kilograms: "))
rate = float(input("Enter the shipping rate per kilogram: "))

## Calculate shipping cost
shipping_cost = weight * rate

## Display the result
print(f"Shipping Cost: {shipping_cost} USD")

