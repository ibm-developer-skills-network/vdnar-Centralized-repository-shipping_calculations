class ShippingCalculator:
    def __init__(self, base_rate_per_km=0.5, base_rate_per_kg=2.0):
        self.base_rate_per_km = base_rate_per_km
        self.base_rate_per_kg = base_rate_per_kg
        self.discount_threshold = 100  
        self.discount_rate = 0.10      

    def calculate_shipping_cost(self, weight, distance, method, destination_country, insurance=False):
        cost = self.calculate_base_cost(weight, distance)
        cost = self.apply_shipping_method(cost, method)
        cost = self.apply_destination_surcharge(cost, destination_country)
        cost = self.apply_insurance(cost, insurance)
        cost = self.apply_discount(cost)
        return cost

    def calculate_base_cost(self, weight, distance):
        return self.base_rate_per_km * distance + self.base_rate_per_kg * weight

    def apply_shipping_method(self, cost, method):
        if method == "express":
            return cost * 1.5  # 50% surcharge for express shipping
        elif method == "standard":
            return cost * 1.2  # 20% surcharge for standard shipping
        else:  # economy
            return cost

    def apply_destination_surcharge(self, cost, country):
        # Example of destination-specific surcharges
        if country.lower() == "us":
            return cost * 1.10  # 10% surcharge for shipping to the US
        elif country.lower() == "canada":
            return cost * 1.15  # 15% surcharge for shipping to Canada
        elif country.lower() == "australia":
            return cost * 1.20  # 20% surcharge for shipping to Australia
        else:
            return cost  # No surcharge for other countries

    def apply_insurance(self, cost, insurance):
        if insurance:
            return cost + 15  # Flat fee for shipping insurance
        return cost

    def apply_discount(self, cost):
        if cost > self.discount_threshold:
            return cost * (1 - self.discount_rate)  
        return cost

    def display_shipping_methods(self):
        print("Available shipping methods: economy, standard, express")



if __name__ == "__main__":
    calc = ShippingCalculator()
    calc.display_shipping_methods()

    # User inputs for shipment details
    weight = float(input("Enter package weight (in kg): "))
    distance = float(input("Enter distance to destination (in km): "))
    method = input("Enter shipping method (economy, standard, express): ").lower()
    country = input("Enter destination country: ").lower()
    insurance = input("Do you want insurance? (yes/no): ").lower() == "yes"

    cost = calc.calculate_shipping_cost(weight, distance, method, country, insurance)
    print(f"The total shipping cost is: ${cost:.2f}")

