import unittest
from Strings import convert_to_lowercase

class TestConvertToLowercase(unittest.TestCase):

    def test_valid_lowercase_conversion(self):
        self.assertEqual(convert_to_lowercase("HELLO"), "hello")
        self.assertEqual(convert_to_lowercase("Hello World"), "hello world")
        self.assertEqual(convert_to_lowercase("123ABC"), "123abc")
        self.assertEqual(convert_to_lowercase(""), "")
        self.assertEqual(convert_to_lowercase("already lowercase"), "already lowercase")

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            convert_to_lowercase(None)
        with self.assertRaises(TypeError):
            convert_to_lowercase(12345)
        with self.assertRaises(TypeError):
            convert_to_lowercase(["HELLO", "WORLD"])
        with self.assertRaises(TypeError):
            convert_to_lowercase({"key": "value"})

if __name__ == "__main__":
    unittest.main()
