import contextlib
import os
import unittest
from io import StringIO
from unittest.mock import patch
import views.credit_view


class TestCreditViewDisplayMonthlyInstallments(unittest.TestCase):
    def test_display_monthly_installments(self):
        view = views.credit_view.CreditView()

        captured_output = StringIO()

        with contextlib.redirect_stdout(captured_output):
            installments = [(340000.00, 8), (230000.00, 8.1)]
            view.display_monthly_installments(installments)

        printed_output = captured_output.getvalue()

        # Define the expected output
        expected_output = (
            "tahun 1 : Rp. 340,000.00/bulan, Suku Bunga : 8%\n"
            "tahun 2 : Rp. 230,000.00/bulan, Suku Bunga : 8.1%\n"
        )

        # Assert that the printed output matches the expected output
        self.assertEqual(printed_output, expected_output)


class TestCreditViewGetInput(unittest.TestCase):
    @patch('builtins.input', side_effect=["Motor", "Baru", "2023", "1000000", "5", "50000"])
    def test_get_input(self, mock_input):
        view = views.credit_view.CreditView()
        user_input = view.get_input()

        self.assertEqual(user_input["vehicle_type"], "motor")
        self.assertEqual(user_input["condition"], "baru")
        self.assertEqual(user_input["year"], "2023")
        self.assertEqual(user_input["total_credit"], "1000000")
        self.assertEqual(user_input["tenure"], "5")
        self.assertEqual(user_input["down_payment"], "50000")


class TestCreditViewGetInputFromFile(unittest.TestCase):
    def test_valid_input(self):
        # Create a temporary test file with known input
        with open('test_input.txt', 'w') as test_file:
            test_file.write("Mobil\nBaru\n2022\n75000000\n2\n35000000")

        view = views.credit_view.CreditView()
        input_data = view.get_input_from_file('test_input.txt')

        # Define the expected output based on the known input
        expected_output = {
            "vehicle_type": "Mobil",
            "condition": "Baru",
            "year": 2022,
            "total_credit": 75000000.0,
            "tenure": 2,
            "down_payment": 35000000.0,
        }

        self.assertEqual(input_data, expected_output)
        os.remove('test_input.txt')

    def test_invalid_input(self):
        with open('test_input.txt', 'w') as test_file:
            test_file.write("Mobil\nBaru\n2022\n75000000")

        with self.assertRaises(ValueError):
            view = views.credit_view.CreditView()
            view.get_input_from_file('test_input.txt')

        os.remove('test_input.txt')


if __name__ == "__main__":
    unittest.main()
