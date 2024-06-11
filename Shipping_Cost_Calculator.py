# Shipping Cost Calculator

## Input package weight and shipping rate
weight = float(input("Enter the package weight in kilograms: "))
rate = float(input("Enter the shipping rate per kilogram: "))

## Calculate shipping cost
shipping_cost = weight * rate

## Display the result
print(f"Shipping Cost: {shipping_cost} USD")
 # Here is a new update by <LaurenSto>
git config --global user.email "stockton4stars@gmail.com"
git config --global user.name "LaurenSto"
git add .
git commit -m "added a new line to Shipping_Cost_Calculator.py"
git status
git push --set-upstream origin shipping_calculator_fixes
