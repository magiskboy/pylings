import unittest

from pylings.ex_for_beginner import divisible_of_five

TEST_CASES = [
    {"input": {"numbers": [0, 1, 2, 3, 4, 5]}, "expect": [0, 5]},
    {"input": {"numbers": []}, "expect": []},
    {"input": {"numbers": [125, 134, 78, 90]}, "expect": [125, 90]},
]


class DivisibleOfFiveTestCase(unittest.TestCase):
    def test_(self):
        for test_case in TEST_CASES:
            actual = divisible_of_five.main(**test_case["input"])
            self.assertListEqual(test_case["expect"], actual)
