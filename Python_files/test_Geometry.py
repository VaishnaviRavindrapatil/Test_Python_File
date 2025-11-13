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


# ---- Auto-generated tests ----
import unittest
from Geometry import calculate_rectangle_perimeter

class TestCalculateRectanglePerimeter(unittest.TestCase):

    def test_valid_perimeter(self):
        # Test with valid positive integers
        self.assertEqual(calculate_rectangle_perimeter(5, 10), 30)
        self.assertEqual(calculate_rectangle_perimeter(7, 3), 20)
        self.assertEqual(calculate_rectangle_perimeter(0, 0), 0)
        self.assertEqual(calculate_rectangle_perimeter(1, 1), 4)

        # Test with valid positive floats
        self.assertAlmostEqual(calculate_rectangle_perimeter(5.5, 10.2), 31.4)
        self.assertAlmostEqual(calculate_rectangle_perimeter(7.1, 3.3), 20.8)

    def test_negative_dimensions(self):
        # Test with negative dimensions
        with self.assertRaises(ValueError):
            calculate_rectangle_perimeter(-5, 10)
        with self.assertRaises(ValueError):
            calculate_rectangle_perimeter(5, -10)
        with self.assertRaises(ValueError):
            calculate_rectangle_perimeter(-5, -10)

    def test_non_numeric_inputs(self):
        # Test with non-numeric inputs
        with self.assertRaises(TypeError):
            calculate_rectangle_perimeter("5", 10)
        with self.assertRaises(TypeError):
            calculate_rectangle_perimeter(5, "10")
        with self.assertRaises(TypeError):
            calculate_rectangle_perimeter("5", "10")
        with self.assertRaises(TypeError):
            calculate_rectangle_perimeter(None, 10)
        with self.assertRaises(TypeError):
            calculate_rectangle_perimeter(5, None)

    def test_missing_arguments(self):
        # Test with missing arguments
        with self.assertRaises(TypeError):
            calculate_rectangle_perimeter(5)
        with self.assertRaises(TypeError):
            calculate_rectangle_perimeter()

if __name__ == '__main__':
    unittest.main()
