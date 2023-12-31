import unittest
from unittest.mock import patch, Mock

from controllers.credit_controller import CreditController


class TestCreditControllerLoadExistingMenu(unittest.TestCase):
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


class TestCreditControllerCalculateNewInput(unittest.TestCase):
    @patch("controllers.credit_controller.CreditView.get_input")
    @patch("controllers.credit_controller.CreditView.display_monthly_installments")
    def test_calculate_new_input_ok(self, mock_display, mock_input):
        # Create a mock response object
        mock_input.return_value = {
            "vehicle_type": "mobil",
            "condition": "baru",
            "year": "2023",
            "total_credit": "1000000",
            "tenure": "3",
            "down_payment": "750000"
        }

        controller = CreditController()
        controller.calculate_new_input()

        expected_installments = [(22500.0, 8), (24322.5, 8.1), (26414.235, 8.6)]
        mock_display.assert_called_with(expected_installments)

    @patch("controllers.credit_controller.CreditView.get_input")
    @patch("controllers.credit_controller.CreditView.display_monthly_installments")
    def test_calculate_new_input_invalid_vehicle(self, mock_display, mock_input):
        # Create a mock response object
        mock_input.return_value = {
            "vehicle_type": "motor",
            "condition": "baru",
            "year": "2029",
            "total_credit": "1000000",
            "tenure": "5",
            "down_payment": "50000"
        }

        controller = CreditController()
        controller.calculate_new_input()

        mock_display.assert_not_called()


class TestCreditControllerCalculateNewInputFromFile(unittest.TestCase):
    @patch("controllers.credit_controller.CreditView.get_input_from_file")
    @patch("controllers.credit_controller.CreditView.display_monthly_installments")
    def test_ok(self, mock_display, mock_input):
        # Create a mock response object
        mock_input.return_value = {
            "vehicle_type": "mobil",
            "condition": "baru",
            "year": "2023",
            "total_credit": "1000000",
            "tenure": "3",
            "down_payment": "750000"
        }

        controller = CreditController()
        controller.calculate_new_input_from_file(filename="haha.txt")

        expected_installments = [(22500.0, 8), (24322.5, 8.1), (26414.235, 8.6)]
        mock_display.assert_called_with(expected_installments)

    @patch("controllers.credit_controller.CreditView.get_input_from_file")
    @patch("controllers.credit_controller.CreditView.display_monthly_installments")
    def test_invalid_vehicle(self, mock_display, mock_input):
        # Create a mock response object
        mock_input.return_value = {
            "vehicle_type": "motor",
            "condition": "baru",
            "year": "2029",
            "total_credit": "1000000",
            "tenure": "5",
            "down_payment": "50000"
        }

        controller = CreditController()
        controller.calculate_new_input_from_file(filename="haha.txt")

        mock_display.assert_not_called()


if __name__ == "__main__":
    unittest.main()
