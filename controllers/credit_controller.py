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
            vehicle_type = user_input["vehicle_type"]
            condition = user_input["condition"]
            year = int(user_input["year"])
            total_credit = int(user_input["total_credit"])
            tenure = int(user_input["tenure"])
            down_payment = int(user_input["down_payment"])

            vehicle = models.credits.Vehicle(
                vehicle_type=vehicle_type,
                condition=condition,
                year=year
            )
            vehicle.validate()

            credit = models.credits.Credit(
                vehicle=vehicle,
                total_credit=total_credit,
                down_payment=down_payment,
                tenure=tenure
            )
            credit.validate()

            installments = credit.calculate_monthly_installments()

            self.view.display_monthly_installments(installments)
        except Exception as e:
            print(str(e))

    def load_existing_menu(self):
        try:
            data = self.fetch_data()
            vehicle = models.credits.Vehicle(
                vehicle_type=data.get("vehicleModel").get("vehicleType"),
                condition=data.get("vehicleModel").get("vehicleCondition"),
                year=int(data.get("vehicleModel").get("tahunMobil")))
            vehicle.validate()

            credit = models.credits.Credit(vehicle=vehicle,
                                           total_credit=int(data.get("vehicleModel").get("jumlahPinjaman")),
                                           down_payment=int(data.get("vehicleModel").get("jumlahDownPayment")),
                                           tenure=int(data.get("vehicleModel").get("tenorCicilan")))
            credit.validate()

            installments = credit.calculate_monthly_installments()

            self.view.display_monthly_installments(installments)
        except Exception as e:
            print(str(e))

