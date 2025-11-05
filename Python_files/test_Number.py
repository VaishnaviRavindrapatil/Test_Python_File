import unittest
from Number import add_numbers



class TestAdd_numbers(unittest.TestCase):
    def test_add_numbers_with_valid_integers(self):
        result = Number.add_numbers(3, 5)
        self.assertEqual(result, 8)
    def test_add_numbers_with_valid_floats(self):
        result = Number.add_numbers(2.5, 3.5)
        self.assertEqual(result, 6.0)
    def test_add_numbers_with_integer_and_float(self):
        result = Number.add_numbers(4, 5.5)
        self.assertEqual(result, 9.5)
    def test_add_numbers_with_negative_numbers(self):
        result = Number.add_numbers(-2, -3)
        self.assertEqual(result, -5)
    def test_add_numbers_with_zero(self):
        result = Number.add_numbers(0, 5)
        self.assertEqual(result, 5)
    def test_add_numbers_with_large_numbers(self):
        result = Number.add_numbers(1_000_000, 2_000_000)
        self.assertEqual(result, 3_000_000)
    def test_add_numbers_with_strings_should_raise_typeerror(self):
        with self.assertRaises(TypeError):
            Number.add_numbers("3", "5")
    def test_add_numbers_with_none_should_raise_typeerror(self):
        with self.assertRaises(TypeError):
            Number.add_numbers(None, 5)
    def test_add_numbers_with_list_should_raise_typeerror(self):
        with self.assertRaises(TypeError):
            Number.add_numbers([1, 2], 3)
    def test_add_numbers_with_dict_should_raise_typeerror(self):
        with self.assertRaises(TypeError):
            Number.add_numbers({"a": 1}, {"b": 2})
    def test_add_numbers_with_mixed_invalid_types_should_raise_typeerror(self):
        with self.assertRaises(TypeError):
            Number.add_numbers(3, "5")

if __name__ == '__main__':
    unittest.main()


class TestDivide_numbers(unittest.TestCase):
    def test_divide_numbers_valid_integers():
        result = Number.divide_numbers(10, 2)
        assert result == 5
    def test_divide_numbers_valid_floats():
        result = Number.divide_numbers(7.5, 2.5)
        assert result == 3.0
    def test_divide_numbers_negative_dividend():
        result = Number.divide_numbers(-10, 2)
        assert result == -5
    def test_divide_numbers_negative_divisor():
        result = Number.divide_numbers(10, -2)
        assert result == -5
    def test_divide_numbers_both_negative():
        result = Number.divide_numbers(-10, -2)
        assert result == 5
    def test_divide_numbers_zero_dividend():
        result = Number.divide_numbers(0, 5)
        assert result == 0
    def test_divide_numbers_zero_divisor_raises_exception():
        with pytest.raises(ZeroDivisionError):
            Number.divide_numbers(10, 0)
    def test_divide_numbers_large_numbers():
        result = Number.divide_numbers(1e10, 2)
        assert result == 5e9
    def test_divide_numbers_small_numbers():
        result = Number.divide_numbers(0.0001, 0.01)
        assert result == 0.01
    def test_divide_numbers_non_numeric_inputs_raises_exception():
        with pytest.raises(TypeError):
            Number.divide_numbers("10", 2)
    def test_divide_numbers_divisor_as_none_raises_exception():
        with pytest.raises(TypeError):
            Number.divide_numbers(10, None)
    def test_divide_numbers_dividend_as_none_raises_exception():
        with pytest.raises(TypeError):
            Number.divide_numbers(None, 2)
    def test_divide_numbers_both_inputs_as_none_raises_exception():
        with pytest.raises(TypeError):
            Number.divide_numbers(None, None)
    def test_divide_numbers_divisor_as_boolean():
        result = Number.divide_numbers(10, True)
        assert result == 10  # True is treated as 1 in Python
    def test_divide_numbers_dividend_as_boolean():
        result = Number.divide_numbers(False, 5)
        assert result == 0  # False is treated as 0 in Python

if __name__ == '__main__':
    unittest.main()
