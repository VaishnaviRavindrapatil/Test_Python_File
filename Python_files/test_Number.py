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
