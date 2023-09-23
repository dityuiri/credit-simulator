import contextlib
import unittest
from io import StringIO
import views.credit_view


class TestCreditView(unittest.TestCase):
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

if __name__ == "__main__":
    unittest.main()
