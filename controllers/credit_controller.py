import requests
import json
import config
import models.credits

from views.credit_view import CreditView


class CreditController:
    def __init__(self):
        self.api_url = config.MENU_LOAD_PATH
        self.view = CreditView()

    def fetch_data(self):
        response = requests.get(self.api_url)
        if response.status_code == 200:
            return json.loads(response.text)
        else:
            raise Exception(f"Failed to retrieve data. Status code: {response.status_code}")

    def calculate_new_input(self):
        user_input = self.view.get_input()
        try:
            credit = self.create_and_validate_credit(
                vehicle_type=user_input["vehicle_type"],
                condition=user_input["condition"],
                year=user_input["year"],
                total_credit=user_input["total_credit"],
                down_payment=user_input["down_payment"],
                tenure=user_input["tenure"],
            )

            installments = credit.calculate_monthly_installments()
            self.view.display_monthly_installments(installments)
        except Exception as e:
            print(f'Error: {str(e)}')

    def calculate_new_input_from_file(self, filename):
        file_input = self.view.get_input_from_file(filename)
        try:
            credit = self.create_and_validate_credit(
                vehicle_type=file_input["vehicle_type"],
                condition=file_input["condition"],
                year=file_input["year"],
                total_credit=file_input["total_credit"],
                down_payment=file_input["down_payment"],
                tenure=file_input["tenure"],
            )

            installments = credit.calculate_monthly_installments()
            self.view.display_monthly_installments(installments)
        except Exception as e:
            print(f'Error: {str(e)}')

    def load_existing_menu(self):
        try:
            data = self.fetch_data()
            credit = self.create_and_validate_credit(
                vehicle_type=data.get("vehicleModel").get("vehicleType"),
                condition=data.get("vehicleModel").get("vehicleCondition"),
                year=data.get("vehicleModel").get("tahunMobil"),
                total_credit=data.get("vehicleModel").get("jumlahPinjaman"),
                down_payment=data.get("vehicleModel").get("jumlahDownPayment"),
                tenure=data.get("vehicleModel").get("tenorCicilan"),
            )

            installments = credit.calculate_monthly_installments()
            self.view.display_monthly_installments(installments)
        except Exception as e:
            print(f'Error: {str(e)}')

    @staticmethod
    def create_and_validate_credit(vehicle_type, condition, year, total_credit, down_payment, tenure):
        vehicle = models.credits.Vehicle(
            vehicle_type=vehicle_type,
            condition=condition,
            year=int(year))
        vehicle.validate()

        credit = models.credits.Credit(vehicle=vehicle,
                                       total_credit=int(total_credit),
                                       down_payment=int(down_payment),
                                       tenure=int(tenure))

        credit.validate()

        return credit
