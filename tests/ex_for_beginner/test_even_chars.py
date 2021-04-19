import unittest

from pylings.ex_for_beginner import even_chars

TEST_CASES = [
    {"input": {"string": ""}, "expect": []},
    {"input": {"string": "0123456789"}, "expect": ["0", "2", "4", "6", "8"]},
]


class EvenCharsTestCase(unittest.TestCase):
    def test_(self):
        for test_case in TEST_CASES:
            actual = even_chars.main(**test_case["input"])
            self.assertListEqual(test_case["expect"], actual)
