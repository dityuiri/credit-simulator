from views.helpers import format_currency


class CreditView:
    @staticmethod
    def display_monthly_installments(installments):
        for year, installment in enumerate(installments, start=1):
            print(f"tahun {year} : {format_currency(installment[0])}/bulan, Suku Bunga : {installment[1]}%")

    @staticmethod
    def get_input():
        vehicle_type = input("Enter Vehicle Type (Motor/Mobil): ").strip().lower()
        condition = input("Is the vehicle New or Bekas (Baru/Bekas): ").strip().lower()
        year = input("Enter Vehicle Year (4 digits): ").strip()
        total_credit = input("Enter Total Credit Amount (in Rupiah): ").strip()
        tenure = input("Enter Loan Tenure (1-6 years): ").strip()
        down_payment = input("Enter Down Payment (in Rupiah): ").strip()

        return {
            "vehicle_type": vehicle_type,
            "condition": condition,
            "year": year,
            "total_credit": total_credit,
            "tenure": tenure,
            "down_payment": down_payment,
        }

