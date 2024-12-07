# Edited shipping_calculator.py
def calculate_shipping(weight, distance, priority=False):
    rate = 0.5 if not priority else 1.0
    return weight * distance * rate


