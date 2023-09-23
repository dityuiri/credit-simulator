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

    @staticmethod
    def get_input_from_file(filename):
        with open(filename, 'r') as file:
            lines = file.read().splitlines()
            if len(lines) != 6:
                raise ValueError("Input file must contain exactly 6 lines")

            vehicle_type, condition, year, total_credit, tenure, down_payment = lines
            return {
                "vehicle_type": vehicle_type,
                "condition": condition,
                "year": int(year),
                "total_credit": float(total_credit),
                "tenure": int(tenure),
                "down_payment": float(down_payment),
            }
