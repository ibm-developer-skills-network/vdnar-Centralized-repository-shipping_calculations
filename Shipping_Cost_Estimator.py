class ShippingCalculator:
    def __init__(self):
        # Base rates per kg for different shipping methods
        self.shipping_rates = {
            'ground': 5.00,    # $5.00 per kg
            'express': 12.50,  # $12.50 per kg
            'overnight': 25.00 # $25.00 per kg
        }

        # Distance multipliers (example zones)
        self.zone_multipliers = {
            'local': 1.0,      # Within same city
            'regional': 1.3,   # Within same region/state
            'national': 1.8,   # Within country
            'international': 2.5 # International shipping
        }

    def calculate_cost(self, weight_kg, shipping_method, zone, fragile=False):
        """
        Calculate shipping cost based on weight, method, zone, and whether item is fragile

        Args:
            weight_kg (float): Weight of package in kilograms
            shipping_method (str): 'ground', 'express', or 'overnight'
            zone (str): 'local', 'regional', 'national', or 'international'
            fragile (bool): Whether package contains fragile items

        Returns:
            float: Total shipping cost
        """
        # Input validation
        if shipping_method not in self.shipping_rates:
            raise ValueError("Invalid shipping method")
        if zone not in self.zone_multipliers:
            raise ValueError("Invalid shipping zone")
        if weight_kg <= 0:
            raise ValueError("Weight must be greater than 0")

        # Base cost calculation
        base_rate = self.shipping_rates[shipping_method]
        zone_multiplier = self.zone_multipliers[zone]

        # Calculate basic cost
        cost = weight_kg * base_rate * zone_multiplier

        # Add fragile handling fee if applicable (20% extra)
        if fragile:
            cost *= 1.20

        # Add insurance for high-value or international shipments
        if zone == 'international' or cost > 100:
            insurance_fee = cost * 0.05  # 5% insurance fee
            cost += insurance_fee

        # Add fuel surcharge (current market conditions)
        fuel_surcharge = cost * 0.03  # 3% fuel surcharge
        cost += fuel_surcharge

        return round(cost, 2)

def main():
    # Create calculator instance
    calculator = ShippingCalculator()

    # Example usage
    try:
        # Get user input
        weight = float(input("Enter package weight (kg): "))
        print("\nShipping Methods: ground, express, overnight")
        method = input("Enter shipping method: ").lower()
        print("\nZones: local, regional, national, international")
        zone = input("Enter shipping zone: ").lower()
        fragile = input("\nIs the package fragile? (yes/no): ").lower() == 'yes'

        # Calculate and display cost
        cost = calculator.calculate_cost(weight, method, zone, fragile)

        print("\n=== Shipping Cost Summary ===")
        print(f"Weight: {weight} kg")
        print(f"Method: {method}")
        print(f"Zone: {zone}")
        print(f"Fragile: {'Yes' if fragile else 'No'}")
        print(f"Total Cost: ${cost:.2f}")

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()