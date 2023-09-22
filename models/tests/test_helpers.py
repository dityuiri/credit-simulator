from models.helpers import calculate_percentage

import unittest


class TestCalculatePercentage(unittest.TestCase):
    def test_calculate(self):
        expected = 2500
        result = calculate_percentage(10000, 25)
        self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()
