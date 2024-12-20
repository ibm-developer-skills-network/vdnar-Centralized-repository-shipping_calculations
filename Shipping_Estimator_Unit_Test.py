import unittest
from Shipping_Cost_Estimator import ShippingCalculator  # Updated import statement

class TestShippingCalculator(unittest.TestCase):
    def setUp(self):
        """Set up a calculator instance before each test"""
        self.calculator = ShippingCalculator()

    def test_ground_local_shipping(self):
        """Test basic ground shipping within local zone"""
        cost = self.calculator.calculate_cost(1.0, 'ground', 'local', False)
        self.assertEqual(cost, 5.15)  # 5.00 * 1.0 * 1.03 (fuel surcharge)

    def test_fragile_handling(self):
        """Test fragile item handling fee"""
        normal_cost = self.calculator.calculate_cost(1.0, 'ground', 'local', False)
        fragile_cost = self.calculator.calculate_cost(1.0, 'ground', 'local', True)
        self.assertAlmostEqual(fragile_cost, normal_cost * 1.2, places=2)

    def test_international_shipping(self):
        """Test international shipping with insurance"""
        cost = self.calculator.calculate_cost(1.0, 'ground', 'international', False)
        # Base: 5.00 * 2.5 = 12.50
        # Insurance: 12.50 * 0.05 = 0.625
        # Fuel: (12.50 + 0.625) * 0.03 = 0.39375
        expected = 13.52  # 12.50 + 0.625 + 0.39375
        self.assertAlmostEqual(cost, expected, places=2)

    def test_invalid_shipping_method(self):
        """Test invalid shipping method raises ValueError"""
        with self.assertRaises(ValueError):
            self.calculator.calculate_cost(1.0, 'invalid_method', 'local', False)

    def test_invalid_zone(self):
        """Test invalid zone raises ValueError"""
        with self.assertRaises(ValueError):
            self.calculator.calculate_cost(1.0, 'ground', 'invalid_zone', False)

    def test_invalid_weight(self):
        """Test invalid weight raises ValueError"""
        with self.assertRaises(ValueError):
            self.calculator.calculate_cost(-1.0, 'ground', 'local', False)

    def test_high_value_insurance(self):
        """Test insurance is added for high-value shipments"""
        # Create a shipment that costs over $100 before insurance
        cost = self.calculator.calculate_cost(20.0, 'overnight', 'national', False)
        base_cost = 20.0 * 25.0 * 1.8  # weight * overnight_rate * national_multiplier
        self.assertGreater(cost, base_cost * 1.05)  # Should include 5% insurance

    def test_express_regional_shipping(self):
        """Test express shipping to regional zone"""
        cost = self.calculator.calculate_cost(2.0, 'express', 'regional', False)
        # Base: 2.0 * 12.50 * 1.3 = 32.50
        # Fuel: 32.50 * 0.03 = 0.975
        expected = 33.48  # 32.50 + 0.975
        self.assertAlmostEqual(cost, expected, places=2)

if __name__ == '__main__':
    unittest.main()