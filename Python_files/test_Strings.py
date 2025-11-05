import unittest
from Strings import is_palindrome



class TestIs_palindrome(unittest.TestCase):
    def test_is_palindrome_valid_palindrome():
        result = Strings.is_palindrome("racecar")
        assert result is True
    def test_is_palindrome_valid_palindrome_single_character():
        result = Strings.is_palindrome("a")
        assert result is True
    def test_is_palindrome_valid_palindrome_empty_string():
        result = Strings.is_palindrome("")
        assert result is True
    def test_is_palindrome_valid_palindrome_with_spaces():
        result = Strings.is_palindrome("A man a plan a canal Panama")
        assert result is True
    def test_is_palindrome_valid_palindrome_mixed_case():
        result = Strings.is_palindrome("RaceCar")
        assert result is True
    def test_is_palindrome_valid_palindrome_with_numbers():
        result = Strings.is_palindrome("12321")
        assert result is True
    def test_is_palindrome_invalid_not_palindrome():
        result = Strings.is_palindrome("hello")
        assert result is False
    def test_is_palindrome_invalid_mixed_case_not_palindrome():
        result = Strings.is_palindrome("Hello")
        assert result is False
    def test_is_palindrome_invalid_with_special_characters():
        result = Strings.is_palindrome("hello!")
        assert result is False
    def test_is_palindrome_invalid_numbers_not_palindrome():
        result = Strings.is_palindrome("12345")
        assert result is False

if __name__ == '__main__':
    unittest.main()
