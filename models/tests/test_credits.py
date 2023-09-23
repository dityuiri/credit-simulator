import datetime
import unittest

from models.constants import VEHICLE_TYPE_CAR, VEHICLE_CONDITION_NEW, VEHICLE_TYPE_MOTORCYCLE, VEHICLE_CONDITION_OLD
from models.credits import Vehicle, Credit


class TestVehicle(unittest.TestCase):
    def test_init_vehicle(self):
        vehicle = Vehicle(VEHICLE_TYPE_CAR, VEHICLE_CONDITION_NEW, 2023)
        self.assertEqual(vehicle.vehicle_type, VEHICLE_TYPE_CAR)
        self.assertEqual(vehicle.condition, VEHICLE_CONDITION_NEW)
        self.assertEqual(vehicle.year, 2023)

    def test_empty_type(self):
        with self.assertRaises(ValueError):
            Vehicle("", VEHICLE_CONDITION_NEW, 2023).validate()

    def test_invalid_vehicle_type(self):
        with self.assertRaises(ValueError):
            Vehicle("InvalidType", VEHICLE_CONDITION_NEW, 2023).validate()

    def test_empty_condition(self):
        with self.assertRaises(ValueError):
            Vehicle(VEHICLE_TYPE_CAR, "", 2023).validate()

    def test_invalid_condition(self):
        with self.assertRaises(ValueError):
            Vehicle(VEHICLE_TYPE_CAR, "InvalidCondition", 2023).validate()

    def test_invalid_year(self):
        with self.assertRaises(ValueError):
            Vehicle(VEHICLE_TYPE_CAR, VEHICLE_CONDITION_NEW, 999).validate()

    def test_invalid_new_vehicle_year(self):
        current_year = datetime.datetime.now().year
        invalid_year = current_year + 32
        with self.assertRaises(ValueError):
            Vehicle(VEHICLE_TYPE_CAR, VEHICLE_CONDITION_NEW, invalid_year).validate()


class TestCredit(unittest.TestCase):
    def test_init_credit(self):
        vehicle = Vehicle(VEHICLE_TYPE_CAR, VEHICLE_CONDITION_NEW, 2023)
        credit = Credit(vehicle, 20000, 8000, 36)
        self.assertEqual(credit.total_credit, 20000)
        self.assertEqual(credit.down_payment, 8000)
        self.assertEqual(credit.tenure, 36)

    def test_invalid_total_credit(self):
        vehicle = Vehicle(VEHICLE_TYPE_CAR, VEHICLE_CONDITION_NEW, 2023)
        with self.assertRaises(ValueError):
            Credit(vehicle, "InvalidCredit", 2000, 5).validate()

    def test_invalid_tenure(self):
        vehicle = Vehicle(VEHICLE_TYPE_CAR, VEHICLE_CONDITION_NEW, 2023)
        with self.assertRaises(ValueError):
            Credit(vehicle, 10000, 2000, 20).validate()

    def test_invalid_down_payment(self):
        vehicle = Vehicle(VEHICLE_TYPE_CAR, VEHICLE_CONDITION_NEW, 2023)
        with self.assertRaises(ValueError):
            Credit(vehicle, 10000, "InvalidDownPayment", 5).validate()

    def test_calculate_monthly_installments_car(self):
        vehicle = Vehicle(VEHICLE_TYPE_CAR, VEHICLE_CONDITION_NEW, 2023)
        credit = Credit(vehicle, 100000000, 75000000, 3)
        results = credit.calculate_monthly_installments()

        self.assertEqual(3, len(results))
        self.assertEqual(2250000.00, results[0][0])
        self.assertEqual(8, results[0][1])
        self.assertEqual(2432250.00, results[1][0])
        self.assertEqual(8.1, results[1][1])
        self.assertEqual(2641423.50, results[2][0])
        self.assertEqual(8.6, results[2][1])

    def test_calculate_monthly_installments_motorcycle(self):
        vehicle = Vehicle(VEHICLE_TYPE_MOTORCYCLE, VEHICLE_CONDITION_OLD, 2023)
        credit = Credit(vehicle, 100000000, 75000000, 2)
        results = credit.calculate_monthly_installments()

        self.assertEqual(2, len(results))
        self.assertEqual(3406250.0, results[0][0])
        self.assertEqual(9, results[0][1])
        self.assertEqual(3716218.75, results[1][0])
        self.assertEqual(9.1, results[1][1])


if __name__ == "__main__":
    unittest.main()
