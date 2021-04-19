import unittest

from pylings.ex_for_beginner import separate_even_odd

TEST_CASES = [
    {
        "input": {"origin": [1, 2, 4, 5, 6, 7, 8]},
        "expect": ([2, 4, 6, 8], [1, 3, 5, 7]),
    },
    {"input": {"origin": [1, 3, 5, 7]}, "expect": ([], [1, 3, 5, 7])},
    {"input": {"origin": [2, 4, 6, 8]}, "expect": ([2, 4, 6, 8], [])},
]


class SeparateEvenOddTestCase(unittest.TestCase):
    def test_(self):
        for test_case in TEST_CASES:
            actual = separate_even_odd.main(**test_case["input"])
            self.assertTupleEqual(test_case["expect"], actual)
