import unittest

from pylings.ex_for_beginner import count_substring

TEST_CASES = [
    {
        "input": {
            "origin": "Emma",
        },
        "expect": 1,
    },
    {
        "input": {
            "origin": "Emmalalaemma",
        },
        "expect": 1,
    },
    {
        "input": {
            "origin": "",
        },
        "expect": 0,
    },
]


class CountSubstringTestCase(unittest.TestCase):
    def test_(self):
        for test_case in TEST_CASES:
            actual = count_substring.main(**test_case["input"])
            self.assertEqual(test_case["expect"], actual)
