import unittest
from Strings import add_special_character

class TestAddSpecialCharacter(unittest.TestCase):

    def test_add_special_character_valid_cases(self):
        # Test adding a special character to a valid string
        self.assertEqual(add_special_character("hello", "!"), "hello!")
        self.assertEqual(add_special_character("world", "@"), "world@")
        self.assertEqual(add_special_character("test123", "#"), "test123#")
        self.assertEqual(add_special_character("python", "$"), "python$")
        self.assertEqual(add_special_character("unittest", "%"), "unittest%")

    def test_add_special_character_empty_string(self):
        # Test adding a special character to an empty string
        self.assertEqual(add_special_character("", "!"), "!")

    def test_add_special_character_empty_character(self):
        # Test adding an empty character to a string
        self.assertEqual(add_special_character("hello", ""), "hello")

    def test_add_special_character_both_empty(self):
        # Test adding an empty character to an empty string
        self.assertEqual(add_special_character("", ""), "")

    def test_add_special_character_invalid_string_type(self):
        # Test invalid string type (non-string input)
        with self.assertRaises(TypeError):
            add_special_character(123, "!")  # Integer as input
        with self.assertRaises(TypeError):
            add_special_character(None, "!")  # None as input
        with self.assertRaises(TypeError):
            add_special_character(["hello"], "!")  # List as input

    def test_add_special_character_invalid_character_type(self):
        # Test invalid character type (non-string input)
        with self.assertRaises(TypeError):
            add_special_character("hello", 123)  # Integer as character
        with self.assertRaises(TypeError):
            add_special_character("hello", None)  # None as character
        with self.assertRaises(TypeError):
            add_special_character("hello", ["!"])  # List as character

    def test_add_special_character_multiple_characters(self):
        # Test adding multiple characters instead of a single special character
        self.assertEqual(add_special_character("hello", "!@"), "hello!@")
        self.assertEqual(add_special_character("world", "#$"), "world#$")

if __name__ == "__main__":
    unittest.main()
