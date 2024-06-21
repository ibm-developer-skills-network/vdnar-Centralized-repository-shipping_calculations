# Shipping Cost Calculator

## Input package weight and shipping rate
weight = float(input("Enter the package weight in kilograms: "))
rate = float(input("Enter the shipping rate per kilogram: "))
inr_exch_rate = float(input("Enter Dollar to INR Exchange rate for today: ")

## Calculate shipping cost
shipping_cost = weight * rate
cost_in_inr = shipping_cost * inr_exch_rate

## Display the result
print(f"Shipping Cost: {shipping_cost} USD")
print(f"Shipping Cost in INR Today: {cost_in_inr} Rupee")

