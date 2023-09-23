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

    def load_existing_menu(self):
        try:
            data = self.fetch_data()
            vehicle = models.credits.Vehicle(
                vehicle_type=data.get("vehicleModel").get("vehicleType"),
                condition=data.get("vehicleModel").get("vehicleCondition"),
                year=int(data.get("vehicleModel").get("tahunMobil")))

            credit = models.credits.Credit(vehicle=vehicle,
                                           total_credit=int(data.get("vehicleModel").get("jumlahPinjaman")),
                                           down_payment=int(data.get("vehicleModel").get("jumlahDownPayment")),
                                           tenure=int(data.get("vehicleModel").get("tenorCicilan")))
            installments = credit.calculate_monthly_installments()

            self.view.display_monthly_installments(installments)
        except Exception as e:
            print(str(e))

