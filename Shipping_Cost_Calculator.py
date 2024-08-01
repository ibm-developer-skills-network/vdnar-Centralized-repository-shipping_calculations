# Shipping Cost Calculator

## Input package weight and shipping rate
weight = float(input("Enter the package weight in kilograms: "))
rate = float(input("Enter the shipping rate per kilogram: "))


## Calculate shipping cost
shipping_cost = weight * rate
rate_of_tax = 0.05
tax = rate_of_tax * shipping_cost
shipping_cost_incl_tax = shipping_cost + tax

## Display the result
print(f"Shipping Cost Including Tax: {shipping_cost} USD + {tax} USD = {shipping_cost_incl_tax} USD")



