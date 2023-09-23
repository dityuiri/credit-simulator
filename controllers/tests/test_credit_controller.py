import unittest
from unittest.mock import patch, Mock
from controllers.credit_controller import CreditController


class TestCreditController(unittest.TestCase):
    @patch("controllers.credit_controller.requests.get")
    @patch("controllers.credit_controller.json.loads")
    @patch("controllers.credit_controller.CreditView.display_monthly_installments")
    def test_load_existing_menu_ok(self, mock_display, mock_json_loads, mock_requests_get):
        # Create a mock response object
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.text = '{"vehicleModel": {"vehicleType": "Mobil", "vehicleCondition": "Baru", "tahunMobil": "2023", "jumlahPinjaman": 1000000, "jumlahDownPayment": 250000, "tenorCicilan": 3}}'
        mock_requests_get.return_value = mock_response
        mock_json_loads.return_value = {
            "vehicleModel": {
                "vehicleType": "Mobil",
                "vehicleCondition": "Baru",
                "tahunMobil": "2023",
                "jumlahPinjaman": 1000000,
                "jumlahDownPayment": 250000,
                "tenorCicilan": 3,
            }
        }

        controller = CreditController()
        controller.load_existing_menu()

        mock_json_loads.assert_called_with(mock_response.text)

        expected_installments = [(7500.0, 8), (8107.5, 8.1), (8804.745, 8.6)]
        mock_display.assert_called_with(expected_installments)

    @patch("controllers.credit_controller.requests.get")
    @patch("controllers.credit_controller.json.loads")
    @patch("controllers.credit_controller.CreditView.display_monthly_installments")
    def test_load_existing_menu_non_200_status_code(self, mock_display, mock_json_loads, mock_requests_get):
        mock_response = Mock()
        mock_response.status_code = 400
        mock_response.text = '{"vehicleModel": {"vehicleType": "Mobil", "vehicleCondition": "Baru", "tahunMobil": "2023", "jumlahPinjaman": 1000000, "jumlahDownPayment": 250000, "tenorCicilan": 3}}'
        mock_requests_get.return_value = mock_response

        controller = CreditController()
        controller.load_existing_menu()

        mock_json_loads.assert_not_called()
        mock_display.assert_not_called()

    @patch("controllers.credit_controller.requests.get")
    @patch("controllers.credit_controller.json.loads")
    @patch("controllers.credit_controller.CreditView.display_monthly_installments")
    def test_load_existing_menu_invalid_vehicle(self, mock_display, mock_json_loads, mock_requests_get):
        # Create a mock response object
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.text = '{"vehicleModel": {"vehicleType": "rumah", "vehicleCondition": "Baru", "tahunMobil": "2023", "jumlahPinjaman": 1000000, "jumlahDownPayment": 250000, "tenorCicilan": 3}}'
        mock_requests_get.return_value = mock_response
        mock_json_loads.return_value = {
            "vehicleModel": {
                "vehicleType": "rumah",
                "vehicleCondition": "Baru",
                "tahunMobil": "2023",
                "jumlahPinjaman": 1000000,
                "jumlahDownPayment": 250000,
                "tenorCicilan": 3,
            }
        }

        controller = CreditController()
        controller.load_existing_menu()

        mock_json_loads.assert_called_with(mock_response.text)
        mock_display.assert_not_called()


if __name__ == "__main__":
    unittest.main()
