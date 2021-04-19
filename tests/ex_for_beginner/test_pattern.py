import unittest

from pylings.ex_for_beginner import pattern
from tests.utils import redirect_stdio


class PatternTestCase(unittest.TestCase):
    def test_with_n_greater_than_zero(self):
        with redirect_stdio() as stdio:
            pattern.main(3)

        self.assertEqual(stdio.stdout.getvalue(), "1\n2 2\n3 3 3\n")

    def test_with_n_equal_zero(self):
        with redirect_stdio() as stdio:
            pattern.main(0)

        self.assertEqual(stdio.stdout.getvalue(), "")
