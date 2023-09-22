from models.constants import VEHICLE_TYPE_CAR, VEHICLE_TYPE_MOTORCYCLE, MAX_CREDIT_LIMIT, MAX_TENURE, MIN_TENURE, \
    VEHICLE_CONDITION_NEW, VEHICLE_CONDITION_OLD, MIN_DOWN_PAYMENT_NEW, MIN_DOWN_PAYMENT_OLD, BASE_INTEREST_RATE_CAR, \
    BASE_INTEREST_RATE_MOTORCYCLE, CREDIT_INTEREST_PER_2YEARS, CREDIT_INTEREST_PER_YEAR
from models.helpers import calculate_percentage

import datetime


class Vehicle:
    def __init__(self, vehicle_type, condition, year):
        self.vehicle_type = vehicle_type
        self.condition = condition
        self.year = year

    def validate(self):
        current_year = datetime.datetime.now().year
        # Value validations
        if not isinstance(self.vehicle_type, str) or not self.vehicle_type:
            raise ValueError("Vehicle type must be a non-empty string")

        if self.vehicle_type.lower() not in [VEHICLE_TYPE_CAR, VEHICLE_TYPE_MOTORCYCLE]:
            raise ValueError(f"Vehicle type must be a '{VEHICLE_TYPE_CAR}' or '{VEHICLE_TYPE_MOTORCYCLE}'")

        if not isinstance(self.condition, str) or not self.condition:
            raise ValueError("Condition must be a non-empty string")

        if self.condition.lower() not in [VEHICLE_CONDITION_NEW, VEHICLE_CONDITION_OLD]:
            raise ValueError(F"Vehicle condition must be '{VEHICLE_CONDITION_NEW}' or '{VEHICLE_CONDITION_OLD}'")

        if not isinstance(self.year, int) or self.year < 1000 or self.year > 9999:
            raise ValueError("Year must be a non-negative integer and 4 digit valid year")

        if self.condition.lower() == VEHICLE_CONDITION_NEW and (self.year < current_year-1 or self.year > current_year):
            raise ValueError("For New vehicle, the year must be in the current year or the previous one")


class Credit:
    def __init__(self, vehicle, total_credit, down_payment, tenure):
        self.vehicle = vehicle
        self.total_credit = total_credit
        self.down_payment = down_payment
        self.tenure = tenure

    def validate(self):
        if not isinstance(self.total_credit, int) or 0 > self.total_credit > MAX_CREDIT_LIMIT:
            raise ValueError("Total credit must be a non-negative integer and not exceeding max credit limit")

        if not isinstance(self.tenure, int) or MIN_TENURE > self.tenure > MAX_TENURE:
            raise ValueError(f"Tenure must be in the range of {MIN_TENURE} - {MAX_TENURE}")

        if not isinstance(self.down_payment, int) or self.down_payment < 0:
            raise ValueError("Down payment must be a non-negative integer")

        min_down_payment = (
            MIN_DOWN_PAYMENT_NEW if self.vehicle.condition == VEHICLE_CONDITION_NEW else MIN_DOWN_PAYMENT_OLD
        )

        if self.down_payment < calculate_percentage(self.total_credit, min_down_payment):
            raise ValueError(f"Minimum down payment for this vehicle must be {min_down_payment}%")

    def get_base_interest_rate(self):
        if self.vehicle.vehicle_type == VEHICLE_TYPE_CAR:
            return BASE_INTEREST_RATE_CAR
        elif self.vehicle.vehicle_type == VEHICLE_TYPE_MOTORCYCLE:
            return BASE_INTEREST_RATE_MOTORCYCLE

    def calculate_monthly_installments(self):
        interest_rate = self.get_base_interest_rate()
        down_payment = self.down_payment
        monthly_installments = []  # we will store it as a set like this (installments, interest_rate)
        for year in range(0, self.tenure):
            total_loan = down_payment + calculate_percentage(down_payment, interest_rate)
            monthly_installment = total_loan / ((12*self.tenure) - 12*year)
            monthly_installments.append((monthly_installment, interest_rate))

            # update for the next iteration
            yearly_installment = monthly_installment * 12
            interest_rate += CREDIT_INTEREST_PER_2YEARS if year % 2 == 0 else CREDIT_INTEREST_PER_YEAR
            down_payment = total_loan - yearly_installment

        return monthly_installments
