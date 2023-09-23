from views.helpers import format_currency

import unittest


class TestHelpers(unittest.TestCase):
    def test_format_currency(self):
        input = 345600.234
        expected = "Rp. 345,600.23"
        result = format_currency(input)
        self.assertEqual(expected, result)


if __name__ == "__main__":
    unittest.main()
