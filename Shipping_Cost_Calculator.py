# Shipping Cost Calculator

## Input package weight and shipping rate
weight = float(input("Enter the package weight in kilograms: "))
rate = float(input("Enter the shipping rate per kilogram: "))

##Extra charge for liquid shippping
liquid = int(input("Does your shipment contain liquids? 1.-Yes 2.-No",))
shipping_cost = weight*rate
if liquid == 1:
## Calculate extra shipping cost for liquid
    shipping_cost = (weight * rate)*1.1
    print("You have an extra charge for liquid shippment of 10%")
    print("Your shipping cost is:", shipping_cost, "USD")
elif liquid == 2:
## Display the result
    shipping_cost = weight * rate
    print("Shipping Cost: USD", shipping_cost)
else:
    print("Incorrect option, we will suppose that the shippment does not include any liquids")
    shipping_cost = (weight * rate)+10
    print("Shipping Cost: USD", shipping_cost)
