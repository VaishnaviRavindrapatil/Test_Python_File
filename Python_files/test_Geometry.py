import unittest
from Geometry import calculate_square_area



class TestCalculate_square_area(unittest.TestCase):
    def test_calculate_square_area_valid_input():
        result = Geometry.calculate_square_area(4)
        assert result == 16
    def test_calculate_square_area_zero_input():
        result = Geometry.calculate_square_area(0)
        assert result == 0
    def test_calculate_square_area_negative_input():
        try:
            Geometry.calculate_square_area(-5)
        except ValueError as e:
            assert str(e) == "Side length cannot be negative"
    def test_calculate_square_area_non_numeric_input():
        try:
            Geometry.calculate_square_area("abc")
        except TypeError as e:
            assert str(e) == "Side length must be a numeric value"
    def test_calculate_square_area_float_input():
        result = Geometry.calculate_square_area(3.5)
        assert result == 12.25
    def test_calculate_square_area_large_input():
        result = Geometry.calculate_square_area(100000)
        assert result == 10000000000

if __name__ == '__main__':
    unittest.main()
