# Shipping Cost Calculator
def shipping_cost(x,y):
    return x * y
    
## Input package weight and shipping rate
weight = float(input("Enter the package weight in kilograms: "))
rate = float(input("Enter the shipping rate per kilogram: "))

## Calculate shipping cost

## Display the result
print(f"Shipping Cost: {shipping_cost(weight, rate)} USD")

