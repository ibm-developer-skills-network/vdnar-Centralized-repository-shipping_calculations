# Shipping Cost Calculator

## Input package weight and shipping rate
try:
    weight = float(input("Enter the package weight in kilograms: "))
    rate = float(input("Enter the shipping rate per kilogram (USD): "))
    
    if weight <= 0 or rate <= 0:
        print("Error: Weight and rate must be positive numbers.")
    else:
        ## Calculate shipping cost
        shipping_cost = weight * rate
        
        ## Apply discount for bulk packages
        if weight > 10:
            discount = 0.10  # 10% discount
            shipping_cost *= (1 - discount)
            print(f"A 10% discount has been applied for bulk shipping!")
        
        ## Display the result
        print(f"Shipping Cost: {shipping_cost:.2f} USD")
except ValueError:
    print("Error: Please enter numeric values for weight and rate.")
