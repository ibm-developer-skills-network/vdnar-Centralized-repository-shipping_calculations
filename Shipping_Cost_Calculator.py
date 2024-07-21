# Shipping Cost Calculator
from currency import exchanger

## Input package weight and shipping rate
weight = float(input("Enter the package weight in kilograms: "))
rate = float(input("Enter the shipping rate per kilogram: "))

## Calculate shipping cost
shipping_cost = weight * rate

## Display the result
# Here is a new update by elazrev

currency = ""
while currency not in ["USD", "ILS", "EUR"]:
    try:
        cur_coin = int(input(f"Choose your currency:\n1-USD\n2-ILS\n3-EUR\n"))
        if int(cur_coin) not in range(1, 4):
            raise Exception
        else:
            match cur_coin:
                case 1:
                    currency = "USD"
                case 2:
                    currency = "ILS"
                case 3:
                    currency = "EUR"

    except:
        print("Something went wrong, try again..")

print(f"Shipping Cost: {exchanger.exchanger(shipping_cost, currency)} {currency}")