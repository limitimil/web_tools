import unittest
from sum_digits import SumDigits


class TestSumDigits(unittest.TestCase):

    def test_sum_digits(self):
        obj = SumDigits("""
            123
            456
            7689
            -10
            0.1
            10e100
        """)
        self.assertListEqual(obj.digits, [123, 456, 7689, 10, 0, 1, 10, 100])
        self.assertEqual(obj.get_sum(), 8389)


if __name__ == '__main__':
    unittest.main()
