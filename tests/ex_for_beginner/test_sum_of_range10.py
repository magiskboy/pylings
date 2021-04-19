import unittest

from pylings.ex_for_beginner import sum_of_range10


class SumOfRange10TestCase(unittest.TestCase):
    def test_(self):
        expect = [1, 3, 6, 10, 15, 21, 28, 36, 45, 55]
        actual = sum_of_range10.main()

        self.assertListEqual(expect, actual)
