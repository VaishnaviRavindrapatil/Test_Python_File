
def length_of_string(s):
    return len(s)


def is_palindrome(s):
    s = s.lower().replace(" ", "")  # Convert to lowercase and remove spaces
    return s == s[::-1]


def is_anagram(str1: str, str2: str) -> bool:
    return sorted(str1) == sorted(str2)


def convert_to_uppercase(input_string: str) -> str:
    return input_string.upper()


def convert_to_lowercase(input_string: str) -> str:
    return input_string.lower()
