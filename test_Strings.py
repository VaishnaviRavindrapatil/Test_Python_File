import unittest
from Strings import convert_to_uppercase

class TestConvertToUppercase(unittest.TestCase):

    def test_valid_lowercase_string(self):
        self.assertEqual(convert_to_uppercase("hello"), "HELLO")

    def test_valid_mixedcase_string(self):
        self.assertEqual(convert_to_uppercase("HeLLo"), "HELLO")

    def test_valid_uppercase_string(self):
        self.assertEqual(convert_to_uppercase("HELLO"), "HELLO")

    def test_empty_string(self):
        self.assertEqual(convert_to_uppercase(""), "")

    def test_string_with_numbers(self):
        self.assertEqual(convert_to_uppercase("hello123"), "HELLO123")

    def test_string_with_special_characters(self):
        self.assertEqual(convert_to_uppercase("hello!@#"), "HELLO!@#")

    def test_string_with_whitespace(self):
        self.assertEqual(convert_to_uppercase("hello world"), "HELLO WORLD")

    def test_numeric_input(self):
        with self.assertRaises(TypeError):
            convert_to_uppercase(12345)

    def test_none_input(self):
        with self.assertRaises(TypeError):
            convert_to_uppercase(None)

    def test_list_input(self):
        with self.assertRaises(TypeError):
            convert_to_uppercase(["hello", "world"])

if __name__ == "__main__":
    unittest.main()
