import unittest

from pylings.ex_for_beginner import product_of_two_int

TEST_CASES = [
    {
        "input": {
            "number1": 20,
            "number2": 30,
        },
        "expect": 1,
    },
    {"input": {"number1": 50, "number2": 50}, "expect": 2500},
]


class ProductofTwoIntTestCase(unittest.TestCase):
    def test_(self):
        for test_case in TEST_CASES:
            actual = product_of_two_int.main(**test_case["input"])
            self.assertEqual(test_case["expect"], actual)
