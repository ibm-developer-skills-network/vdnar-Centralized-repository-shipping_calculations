# Shipping Cost Calculator

## Input package weight and shipping rate
peso = float(input("Ingresa el peso del paquete en kilogramos: "))
tasa = float(input("Ingresa la tasa de envío según el perso en kilogramos"))

## Calculate shipping cost
shipping_cost = peso * tasa

## Display the result
print(f"El costo de envío es : {shipping_cost} CLP")

