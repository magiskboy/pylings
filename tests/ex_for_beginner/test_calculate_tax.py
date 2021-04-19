import unittest

from pylings.ex_for_beginner import calculate_tax

TEST_CASES = [
    {"tax_income": 9000, "expect": 0},
    {"tax_income": 10000, "expect": 0},
    {"tax_income": 15000, "expect": 500},
    {"tax_income": 20000, "expect": 1000},
    {"tax_income": 450000, "expect": 6000},
]


class CalculateTaxTestCase(unittest.TestCase):
    def test_(self):
        for test_case in TEST_CASES:
            actual = calculate_tax.main(test_case["tax_income"])
            self.assertEqual(test_case["expect"], actual)
