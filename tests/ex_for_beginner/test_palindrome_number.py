import unittest

from pylings.ex_for_beginner import palindrome_number

TEST_CASES = [
    {"input": {"n": 1}, "expect": True},
    {"input": {"n": 123321}, "expect": True},
    {"input": {"n": "12321"}, "expect": True},
    {"input": {"n": 1231}, "expect": False},
    {"input": {"n": 12343}, "expect": False},
]


class PalindromeNumberTestCase(unittest.TestCase):
    def test_(self):
        for test_case in TEST_CASES:
            actual = palindrome_number.main(**test_case["input"])
            self.assertEqual(test_case["expect"], actual)
