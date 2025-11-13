import unittest
from Geometry import calculate_circle_perimeter
import math

class TestCalculateCirclePerimeter(unittest.TestCase):

    def test_valid_radius(self):
        # Test with a positive radius
        self.assertAlmostEqual(calculate_circle_perimeter(1), 2 * math.pi * 1)
        self.assertAlmostEqual(calculate_circle_perimeter(5), 2 * math.pi * 5)
        self.assertAlmostEqual(calculate_circle_perimeter(10.5), 2 * math.pi * 10.5)

    def test_zero_radius(self):
        # Test with a radius of zero
        self.assertEqual(calculate_circle_perimeter(0), 0)

    def test_negative_radius(self):
        # Test with a negative radius (should raise ValueError)
        with self.assertRaises(ValueError):
            calculate_circle_perimeter(-1)

    def test_invalid_type(self):
        # Test with invalid types for radius
        with self.assertRaises(TypeError):
            calculate_circle_perimeter("string")
        with self.assertRaises(TypeError):
            calculate_circle_perimeter(None)
        with self.assertRaises(TypeError):
            calculate_circle_perimeter([1, 2, 3])
        with self.assertRaises(TypeError):
            calculate_circle_perimeter({"radius": 5})

if __name__ == "__main__":
    unittest.main()
