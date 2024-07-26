# Shipping Cost Calculator

## Input package weight and shipping rate
weight = input("Enter the package weight in kilograms: ")
while( !weight.isnumeric()):
  weight = input("Please, enter a numeric value : ")
  if(',' in weight and (weight.count('.') <= 1 or weight.count(',') <= 1)):
    weight = weight.replace(",", ".")
    hole_w = weight[:weight.index(".")]]
    decimal_w = weight[weight.index(".") + 1::]
    if(hole_w.isdecimal() and decimal_w.isdecimal()):
      weight = float(weight)
      break;
weight = float(weight)
    
rate = (input("Enter the shipping rate per kilogram: "))
while( !rate.isnumeric()):
  rate = input("Please, enter a numeric value : ")
  if(',' in rate and (rate.count('.') <= 1 or rate.count(',') <= 1)):
    rate = rate.replace(",", ".")
    hole_r = rate[:rate.index(".")]]
    decimal_r = rate[rate.index(".") + 1::]
    if(hole_r.isdecimal() and decimal_r.isdecimal()):
      rate = float(rate)
      break;
rate = float(rate)

## Calculate shipping cost
shipping_cost = weight * rate

## Display the result
print(f"Shipping Cost: {shipping_cost} USD")

