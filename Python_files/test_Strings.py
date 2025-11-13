import unittest
from Strings import is_anagram

class TestIsAnagram(unittest.TestCase):

    def test_valid_anagrams(self):
        self.assertTrue(is_anagram("listen", "silent"))
        self.assertTrue(is_anagram("evil", "vile"))
        self.assertTrue(is_anagram("dusty", "study"))
        self.assertTrue(is_anagram("night", "thing"))
        self.assertTrue(is_anagram("elbow", "below"))

    def test_invalid_anagrams(self):
        self.assertFalse(is_anagram("hello", "world"))
        self.assertFalse(is_anagram("python", "java"))
        self.assertFalse(is_anagram("test", "tests"))
        self.assertFalse(is_anagram("anagram", "nagaramm"))
        self.assertFalse(is_anagram("listen", "listens"))

    def test_case_insensitivity(self):
        self.assertTrue(is_anagram("Listen", "Silent"))
        self.assertTrue(is_anagram("Evil", "Vile"))
        self.assertTrue(is_anagram("Dusty", "Study"))

    def test_with_spaces(self):
        self.assertTrue(is_anagram("conversation", "voices rant on"))
        self.assertTrue(is_anagram("a gentleman", "elegant man"))
        self.assertFalse(is_anagram("hello world", "world hello!"))

    def test_with_special_characters(self):
        self.assertTrue(is_anagram("dormitory!", "dirty room!"))
        self.assertTrue(is_anagram("a+b=c", "c=b+a"))
        self.assertFalse(is_anagram("hello!", "world?"))

    def test_empty_strings(self):
        self.assertTrue(is_anagram("", ""))
        self.assertFalse(is_anagram("a", ""))
        self.assertFalse(is_anagram("", "b"))

    def test_single_characters(self):
        self.assertTrue(is_anagram("a", "a"))
        self.assertFalse(is_anagram("a", "b"))

if __name__ == "__main__":
    unittest.main()
