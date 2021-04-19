import unittest

from pylings.ex_for_beginner import reverse_integer

TEST_CASES = [
    {"input": {"n": 1}, "expect": "1"},
    {
        "input": {
            "n": 12,
        },
        "expect": "2 1",
    },
    {"input": {"n": 123456}, "expect": "6 5 4 3 2 1"},
]


class ReverseIntegerTestCase(unittest.TestCase):
    def test_(self):
        for test_case in TEST_CASES:
            actual = reverse_integer.main(**test_case["input"])
            self.assertEqual(test_case["expect"], actual)
