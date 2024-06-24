# Shipping Cost Calculator

## Input package weight and shipping rate
weight = float(input("Ingresa el peso del paquete en kilogramos: "))
rate = float(input("Ingresa la tasa de envío según el perso en kilogramos"))

## Calculate shipping cost
shipping_cost = weight * rate

## Display the result
print(f"El costo de envío es : {shipping_cost} CLP")

