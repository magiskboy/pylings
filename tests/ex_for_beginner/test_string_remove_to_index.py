import unittest

from pylings.ex_for_beginner import string_remove_to_index

TEST_CASES = [
    {"input": {"origin": "0123456789", "n": 6}, "expect": "789"},
    {"input": {"origin": "0123", "n": 3}, "expect": ""},
    {"input": {"origin": "0123", "n": 2}, "expect": "3"},
    {"input": {"origin": "", "n": 0}, "expect": ""},
]


class StringRemoveToIndexTestCase(unittest.TestCase):
    def test_(self):
        for test_cases in TEST_CASES:
            actual = string_remove_to_index.main(**test_cases["input"])
            self.assertEqual(test_cases["expect"], actual)
