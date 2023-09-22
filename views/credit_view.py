from views.helpers import format_currency


class CreditView:
    @staticmethod
    def display_monthly_installments(installments):
        for year, installment in enumerate(installments, start=1):
            print(f"tahun {year} : {format_currency(installment[0])}/bulan, Suku Bunga : {installment[1]}%")

